import streamlit as st
from pages import page1, page2
import boto3
import pandas as pd

def show_page():
        
    # Set a default page in session state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    if("selected_subreddit" not in st.session_state):
        st.session_state.selected_subreddit = None

    # Navigation function
    def navigate_to(page):
        st.session_state.current_page = page


    try:

        # Get a file from S3 
        s3 = boto3.client('s3')
        subredditnamefile = s3.download_file('reddit-moderator-s3', 'top_subreddits_cleaned.csv', 'top_subreddits_cleaned.csv')

        # Read csv 

        df = pd.read_csv('top_subreddits_cleaned.csv')

        subreddit_list = df["Subreddits"].values

        subreddit_list = ["r/"+subreddit for subreddit in subreddit_list]

    except Exception as e:
        print(e)
        subreddit_list = ["No subreddits found"]




    st.set_page_config(page_title="Multi-Page Streamlit App", layout="wide")

    st.write("CREATED BY ONLY BHAVINKUMAR. NOT AASTHA")

    option = st.selectbox(
        "Select a Subreddit to inspect!",
        tuple(subreddit_list),
    )

    if option != "No subreddits found":
        st.session_state.selected_subreddit = option

    if st.button("Go to the Subreddit Dashboard"):
        navigate_to("Subreddit Dashboard")