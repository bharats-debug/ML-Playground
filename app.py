import streamlit as st

st.title("ML Playground")
st.write("This app will grow into a full machine learning web application over 100 days.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}! Let's build something great.")