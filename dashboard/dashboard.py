import streamlit as st
import requests

st.title("📄 EdgeScan Dashboard")

response = requests.get("http://localhost:5000/docs")
documents = response.json()

st.write("### Scanned Documents")
for doc in documents:
    st.write(f"**{doc['name']}** — *{doc['label']}* at {doc['timestamp']}")