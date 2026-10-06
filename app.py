import streamlit as st

st.set_page_config(
    page_title="AI Presentation Coach",
    page_icon="🎤"
)

st.title("🎤 AI Presentation Coach")

st.write("Your AI Presentation Coach is working!")

st.subheader("📄 Upload Your Presentation")

uploaded_file = st.file_uploader(
    "Choose your PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("✅ PDF uploaded successfully!")
    st.write("File name:", uploaded_file.name)