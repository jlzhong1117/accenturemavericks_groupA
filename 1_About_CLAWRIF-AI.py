import streamlit as st

st.title("About CLAWRIF-AI")
st.header("📄 Technical Details")
st.subheader("📋 Overview")


st.markdown("""**CLAWRIF-AI is an app designed to help users decode the legal jargon in their documents.""")

st.markdown("""##### Backend:""")

st.markdown("""
- **Large Language Model:** Gemini 2.0 Flash  
- **Embedding Model:** Google Gemini Embedding Model - *models/embedding-001*  
- **Vector Store/Database:** FAISS  
- **Orchestration Framework:** LangChain
""")

st.markdown("""##### Frontend:""")
st.markdown("- **Frontend Framework:** StreamlitCloud")

st.write("")

st.subheader("🗄️ FAISS vs. Chroma as a Vector Store/Database")
st.markdown("""
For our vector store/database, we chose **FAISS** instead of **Chroma** due to **cloud deployment compatibility issues** with StreamlitCloud:

- **FAISS** is a **vector index library** designed for **efficient similarity search** on high-dimensional vectors (like embeddings)  
- It’s not a full vector database like Chroma, but it's **lightweight, fast, and ideal for in-memory use**
- **Chroma**, on the other hand, depends on **SQLite ≥ 3.35.0**, which is **not supported on Streamlit Cloud**, leading to deployment errors
- While Chroma is more suited for **production-level applications** with persistence and metadata, **FAISS is perfect for lightweight, local or cloud-compatible RAG applications**
- Since our project is a **small-scale enterprise RAG prototype** with no need for persistent storage or cloud-scale database features, FAISS was the **most reliable and practical choice**
""")


#✅ FAISS works smoothly on **Streamlit Cloud**  
#❌ Chroma does not, due to **SQLite limitations**""")

#instead of Chroma due to cloud compatibility issues with Streamlit Cloud
