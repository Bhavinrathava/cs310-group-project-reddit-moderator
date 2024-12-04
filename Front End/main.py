import streamlit as st
from pages import analyse_subreddit

import boto3

import pandas as pd

from pages import home, subreddit_dashboard, detailed_analysis

# Set a default page in session state
if "current_page" not in st.session_state:
    st.session_state.current_page = "Main"

if "rules" not in st.session_state:
    st.session_state.rules = None

if("selected_subreddit" not in st.session_state):
    st.session_state.selected_subreddit = None

if("posts" not in st.session_state):
    st.session_state.posts = None

# Navigation function
def navigate_to(page):
    st.session_state.current_page = page

if(st.session_state.current_page == "Main"):
    home.show_page()

elif(st.session_state.current_page == "Home"):
    home.show_page()

elif(st.session_state.current_page == "Subreddit Dashboard"):
    subreddit_dashboard.show_page()

elif(st.session_state.current_page == "Analyse Subreddit"):
    analyse_subreddit.show_page()

elif(st.session_state.current_page == "Detailed Analysis"):
    detailed_analysis.show_page()   