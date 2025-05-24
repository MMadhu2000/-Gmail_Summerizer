import streamlit as st
import json
import os

# Set the absolute path to your summaries.json
JSON_PATH = r"summaries.json"

def display_dashboard():
    if not os.path.exists(JSON_PATH):
        st.error("summaries.json not found. Run 2_email_summarizer.py first.")
        return
    
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        summaries = json.load(f)
    
    st.title("📧 Gmail Email Summarizer Dashboard")
    st.caption("Dashboard to view your latest unread email summaries.")
    
    for item in summaries:
        with st.expander(f"Subject: {item['subject']}"):
            st.write(f"Snippet: {item['snippet']}")
            st.markdown("---")
            st.write(f"📝 Summary:\n\n{item['summary']}")

if __name__ == "__main__":
    display_dashboard()
