import streamlit as st
import boto3 

def navigate_to(page):
    st.session_state.current_page = page

def show_page():
    st.title("Subreddit Dashboard")
    st.write("You selected the following subreddit:")
    st.write(st.session_state.selected_subreddit)
    current_subreddit = st.session_state.selected_subreddit

    # Get items from DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('reddit-subreddit-rules')

    # Get items with based on subreddit name 
    response = table.get_item(Key={'subreddit': current_subreddit[2:]})
    item = response['Item']

    st.write("Rules for the selected subreddit:")
    st.write(item['rules'])

    if st.button("Analyse the Subreddit"):
        st.session_state.rules = item['rules']
        navigate_to("Analyse Subreddit")
    
    if st.button("Go back to Home"):
        navigate_to("Home")



