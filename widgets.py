import pandas as pd 
import streamlit as st




st.title("widgets in Python")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

options = st.multiselect(
    "choose your favaourrite language",
    ["Python", "JavaScript", "Java", "C++", "Ruby"]
)

if name and age:    
    st.write(f"Your name is {name} and you are {age} years old.")
    
    
    
uploaded_file = st.file_uploader("Choose a file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)