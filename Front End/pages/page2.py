import streamlit as st

def show_page():
    st.title("Page 2")
    st.write("This is Page 2 of the app!")
    number = st.number_input("Enter a number:", min_value=0, max_value=100)
    st.write(f"You selected: {number}")
