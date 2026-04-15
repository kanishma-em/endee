# ==============================
# SMART AI MEMORY ASSISTANT
# Single-file project using Endee + RAG
# ==============================

import streamlit as st
from sentence_transformers import SentenceTransformer
from endee import Client
from datetime import datetime, timedelta
import openai

# ==============================
# CONFIG
# ==============================

openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="AI Memory Assistant", layout="wide")

# ==============================
# LOAD MODEL & DB
# ==============================

model = SentenceTransformer('all-MiniLM-L6-v2')

client = Client()
collection = client.get_or_create_collection("memory")

# ==============================
# FUNCTIONS
# ==============================

def get_embedding(text):
    return model.encode(text).tolist()

def store_memory(text):
    embedding = get_embedding(text)

    metadata = {
        "timestamp": datetime.now().isoformat()
    }

    collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[str(hash(text + str(datetime.now())))]
    )

def detect_time_filter(query):
    query = query.lower()

    if "today" in query:
        return 1
    elif "last week" in query:
        return 7
    elif "last month" in query:
        return 30

    return None

def retrieve_memory(query, days=None):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    if days:
        filtered_docs = []
        for doc, meta in zip(docs, metas):
            timestamp = datetime.fromisoformat(meta["timestamp"])
            if timestamp > datetime.now() - timedelta(days=days):
                filtered_docs.append(doc)
        return filtered_docs

    return docs

def generate_answer(query, memories):
    context = "\n".join(memories)

    prompt = f"""
    You are an AI assistant.

    Use the following memory context to answer the question.

    Context:
    {context}

    Question:
    {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# ==============================
# UI
# ==============================

st.title("🧠 Smart AI Memory Assistant")

st.sidebar.header("Menu")
mode = st.sidebar.radio("Select Mode", ["Save Memory", "Ask AI"])

user_input = st.text_area("Enter your text here:")

# ==============================
# SAVE MEMORY
# ==============================

if mode == "Save Memory":
    if st.button("Save Memory"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter something!")
        else:
            store_memory(user_input)
            st.success("✅ Memory stored successfully!")

# ==============================
# ASK AI
# ==============================

elif mode == "Ask AI":
    if st.button("Ask"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a question!")
        else:
            days = detect_time_filter(user_input)

            memories = retrieve_memory(user_input, days)

            if not memories:
                st.warning("⚠️ No relevant memories found!")
            else:
                answer = generate_answer(user_input, memories)

                st.subheader("🤖 AI Answer")
                st.write(answer)

                st.subheader("📂 Retrieved Memories")
                for m in memories:
                    st.write("- " + m)

# ==============================
# FOOTER
# ==============================

st.markdown("---")
st.caption("Built using Endee Vector DB + RAG + Streamlit")
