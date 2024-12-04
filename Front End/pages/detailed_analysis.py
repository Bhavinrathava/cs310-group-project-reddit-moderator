import streamlit as st
import pandas as pd

def show_page():
    st.title("Detailed Analysis")
    st.write("This is the detailed analysis page!")
    st.write("The rules for the selected subreddit are:")
    st.write(st.session_state.rules)
    st.write("The posts for the selected subreddit are:")
    
    processed_posts = []

    for post in st.session_state.posts:
        if post["processed_rules"]:
            processed_posts.append(post)
    
    # If there are no processed posts
    if not processed_posts:
        st.write("No processed posts available.")
    else:
        # Create a DataFrame for display
        df = pd.DataFrame([
            {
                "Submission ID": post["submission_id"],
                "Submission Text": post["submission_text"][:30]  # First 30 characters
            }
            for post in processed_posts
        ])
        
        # Display the table using full page width
        st.write("### Processed Posts")
        st.dataframe(df, use_container_width=True)

        # Render each submission's details as a collapsible expander
        for post in processed_posts:
            with st.expander(f"Submission ID: {post['submission_id']}"):
                st.write("Submission Text:")
                st.write(post["submission_text"])
                st.write("Analysis:")
                st.write(post["ollama_output"])  # Replace with actual analysis data

    # Button to go back to Subreddit Dashboard
    if st.button("Go back to Subreddit Dashboard"):
        st.session_state.rules = None
        st.session_state.posts = None
        st.session_state.selected_subreddit = None
        st.session_state.current_page = "Home"
