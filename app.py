import streamlit as st

st.title("ML Playground")
st.write("An interactive app to explore Machine Learning concepts and models.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "What is ML?"])

if page == "Home":
    st.header("Welcome!")
    st.write("This app will grow into a full ML web application over 100 days.")
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Welcome, {name}! Let's build something great.")

elif page == "What is ML?":
    st.header("What is Machine Learning?")
    st.write("""
    Traditional Programming: You write rules + give input → get output.
    
    Machine Learning: You give input + output → machine learns the rules by itself.
    """)
    
    st.subheader("AI vs ML vs DL")
    st.write("""
    - AI: Making machines intelligent like humans.
    - ML: A subset of AI. Machines learn from data without being explicitly programmed.
    - DL: A subset of ML. Uses neural networks to automatically extract features from data.
    """)