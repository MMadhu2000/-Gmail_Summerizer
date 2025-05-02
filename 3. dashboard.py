import streamlit as st
import json
import os

def display_dashboard():
    if not os.path.exists('summaries.json'):
        st.error("❌ summaries.json not found. Run 2_email_summarizer.py first.")
        return
    
    with open('summaries.json', 'r', encoding='utf-8') as f:
        summaries = json.load(f)
    
    st.title("📧 Gmail Email Summarizer Dashboard")
    st.caption("Minimalistic dashboard to view your latest unread email summaries.")
    
    for item in summaries:
        with st.expander(f"Subject: {item['subject']}"):
            st.write(f"📌 Snippet: {item['snippet']}")
            st.markdown("---")
            st.write(f"📝 Summary:\n\n{item['summary']}")

if __name__ == "__main__":
    display_dashboard()
