import streamlit as st
import boto3 
from boto3.dynamodb.conditions import Attr

def navigate_to(page):
    st.session_state.current_page = page

def scan_by_attribute(table, attribute_name, attribute_value):
    try:
        response = table.scan(
            FilterExpression=Attr(attribute_name).eq(attribute_value)
        )
        items = response.get('Items', [])
        return items
    except Exception as e:
        print(f"Error scanning table: {e}")
        return []
    
def show_page():
    st.title("Analysis Dashboard")
    st.write("You selected the following subreddit:")
    st.write(st.session_state.selected_subreddit)
    current_subreddit = st.session_state.selected_subreddit

    # Get items from DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('reddit-submissions')

    # Get items with based on subreddit name 
    response = scan_by_attribute(table, 'subreddit', current_subreddit[2:])
    item = response

    st.session_state.posts = item

    total_submissions = len(item)


    nsfw_processed = 0 
    rule_processed = 0

    for submission in item:
        if submission['processed_rules'] == True:
            rule_processed += 1
        if "label" in submission:
            nsfw_processed += 1

    st.write("Total submissions for the selected subreddit:{} ".format(total_submissions))
    st.write("Total NSFW submissions processed: {}".format(nsfw_processed))
    st.write("Total rule processed submissions: {}".format(rule_processed))

    if st.button("Go back to Home"):
        navigate_to("Home")
    
    if(st.button("Get Detailed Analysis")):
        navigate_to("Detailed Analysis")



