import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Assistente Triador")
st.write("Esta é a versão inicial da interface para triagem de PDFs com IA.")
