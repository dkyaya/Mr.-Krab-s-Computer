import streamlit as st

# Load your custom HTML
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

# Render the HTML inside Streamlit
st.components.v1.html(html, height=800, scrolling=True)
