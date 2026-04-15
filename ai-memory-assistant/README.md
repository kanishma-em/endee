# 🧠 Smart AI Memory Assistant (RAG using Endee)

## 📌 Project Overview

The **Smart AI Memory Assistant** is an AI-powered application that allows users to store, retrieve, and query personal memories using semantic search and Retrieval-Augmented Generation (RAG).

Unlike traditional keyword-based systems, this project uses vector embeddings to understand the meaning of user input and provide intelligent responses based on stored data.

---

## 🚀 Features

* 📝 Store personal notes and memories
* 🔍 Semantic search using vector similarity
* 🤖 AI-generated answers using RAG
* 📅 Time-based filtering (Today, Last Week, Last Month)
* 🖥️ Interactive UI using Streamlit
* ⚡ Fast retrieval using Endee vector database

---

## 🧠 System Architecture

User Input
→ Text Embedding (Sentence Transformers)
→ Stored in Endee Vector Database
→ Query Embedding
→ Similarity Search (Endee)
→ Retrieved Context
→ LLM (OpenAI)
→ Final AI Response

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Vector Database:** Endee
* **Embedding Model:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **LLM:** OpenAI GPT model
* **Frontend/UI:** Streamlit

---

## 📦 How Endee is Used

Endee plays a key role in this project:

* Stores vector embeddings of user memories
* Performs semantic similarity search
* Retrieves the most relevant data for answering queries

This enables efficient and intelligent information retrieval.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install streamlit sentence-transformers endee openai
```

### 3. Add OpenAI API Key

Open `app.py` and replace:

```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 💡 Usage

### ➤ Save Memory

* Select **"Save Memory"**
* Enter text
* Click **Save**

### ➤ Ask AI

* Select **"Ask AI"**
* Ask questions like:

  * “What did I study today?”
  * “What did I learn last week?”

---

## 📁 Project Structure

```
memory-ai/
│── app.py
│── README.md
```

---

## 🎯 Use Cases

* Personal knowledge management
* Study assistant for students
* Memory recall system
* Note-based AI chatbot

---

## 🔮 Future Enhancements

* 🔐 User authentication (multi-user support)
* 🧠 Long-term memory optimization
* 🌐 Cloud deployment
* 📊 Memory analytics dashboard

---

## ⭐ Mandatory Steps (As per Requirement)

Before starting the project:

* ⭐ Star the official Endee repository
* 🍴 Fork the Endee repository
* 🛠️ Build this project on top of your fork

---

## 📜 License

This project is for educational purposes.

---

## 👩‍💻 Author

**Kanishma (Kani)**
B.Tech AI & Data Science Student

---

## 🙌 Acknowledgment

Special thanks to the Endee team for providing a powerful vector database for building AI applications.

