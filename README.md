# 🚀 Retrieval-Augmented Generation (RAG) Application

> **A production-grade, end-to-end Retrieval-Augmented Generation (RAG) system built with Python, LangChain, FAISS, and OpenAI**

---

## 🌟 Overview

This repository implements a **complete RAG (Retrieval-Augmented Generation) pipeline from scratch**, following real-world, enterprise-grade design principles.

The system demonstrates how **raw documents** are:
- ingested
- cleaned
- chunked
- embedded
- indexed in a vector database
- retrieved at query time
- injected into a prompt
- and finally used by an LLM to generate **grounded, factual responses**

This project is **not a demo**.  
It is a **foundation for production RAG systems**.

---

## 🧠 What is Retrieval-Augmented Generation (RAG)?

**RAG** enhances Large Language Models by grounding them in external knowledge.

Instead of relying only on model memory, RAG:

1. Retrieves relevant information from a knowledge base
2. Injects that information into the prompt
3. Generates responses strictly based on retrieved context

### ✅ Benefits
- Reduces hallucinations
- Improves factual accuracy
- Enables domain-specific intelligence
- Scales beyond model context limits

---

## 🏗️ High-Level Architecture
User Query
↓
Embedding Model
↓
FAISS Vector Store
↓
Top-K Relevant Chunks
↓
RAG Prompt Template
↓
LLM (OpenAI via LangChain)
↓
Final Grounded Answer

---

## 📁 Project Structure
├── data_ingestion.py      # Document loading, cleaning, chunking, embeddings
├── vector_store.py        # FAISS vector indexing & similarity search
├── prompt.py              # RAG-aware prompt template
├── llm_model.py           # OpenAI LLM wrapper using LangChain
├── requirements.txt       # Project dependencies
└── README.md              # Documentation

---

## 🔍 Component-Wise Breakdown (A–Z)

### 1️⃣ Data Ingestion (`data_ingestion.py`)

Handles **raw document → vector-ready data**.

#### Responsibilities
- Load documents (PDF / text / CSV via LangChain loaders)
- Clean and normalize text
- Chunk documents into semantic units
- Generate dense embeddings using **Sentence-Transformers (BAAI/bge-m3)**
- Preserve metadata for traceability

#### Outputs
- `embeddings`: NumPy array `(N, 768)`
- `metadata`: document source, chunk index, page info

---

### 2️⃣ Vector Store (`vector_store.py`)

Manages **high-performance similarity search** using FAISS.

#### Responsibilities
- Initialize FAISS index
- Store dense embeddings
- Perform cosine similarity search
- Retrieve Top-K relevant chunks

#### Why FAISS?
- Extremely fast vector search
- Scales to millions of vectors
- CPU & GPU support
- Industry-standard for vector retrieval

---

### 3️⃣ Prompt Engineering (`prompt.py`)

Defines the **RAG-aware system prompt**.

#### Key Design Principles
- LLM answers **only from retrieved context**
- Explicitly prevents hallucinations
- Enforces deterministic, concise responses

#### Behavior
- If answer is not found in context → model says *“I don’t know”*
- Response length constrained to retrieved knowledge

---

### 4️⃣ LLM Interface (`llm_model.py`)

Encapsulates OpenAI models using **LangChain**.

#### Features
- Secure API key loading via environment variables
- Clean abstraction over OpenAI Chat API
- Deterministic inference settings
- Easy model swapping

---

## 🔄 End-to-End Execution Flow

1. Load raw documents
2. Clean and chunk text
3. Generate embeddings
4. Build FAISS index
5. Embed user query
6. Perform similarity search
7. Retrieve Top-K chunks
8. Construct RAG prompt
9. Generate grounded LLM response

---

## ⚙️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python 3.10+ |
| LLM | OpenAI (via LangChain) |
| Embeddings | Sentence-Transformers (BGE-M3) |
| Vector Database | FAISS |
| Framework | LangChain |
| Data Handling | NumPy, Pandas |

---

## 🔐 Security & Best Practices

- API keys via environment variables
- No hard-coded secrets
- Modular & testable design
- Clear separation of concerns
- Production-ready architecture

---

## 🚀 Getting Started
