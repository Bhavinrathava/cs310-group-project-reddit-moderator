import streamlit as st

def show_page():
    st.title("Page 1")
    st.write("This is Page 1 of the app!")
    user_input = st.text_input("Enter something:")
    if user_input:
        st.write(f"You entered: {user_input}")
