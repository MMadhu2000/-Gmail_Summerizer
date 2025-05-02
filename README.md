📜 README.md (full)

# Gmail Email Summarizer Agent 📧🧠

A simple project to fetch unread Gmail emails, summarize them, and display on a minimal dashboard!

---

## 🚀 How it Works

1. **1_gmail_unread_extract.py**  
   Fetches recent unread emails from your Gmail account and saves them into `emails.json`.

2. **2_email_summarizer.py**  
   Reads `emails.json`, summarizes each email's body, and saves into `summaries.json`.

3. **3_dashboard.py**  
   Launches a Streamlit dashboard displaying all email summaries beautifully!

---

## ⚙️ Setup Instructions

1. Install required packages:
   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client transformers streamlit
Enable Gmail API in your Google Cloud Console and download credentials.json into the project folder.
📌 Important: Add in README instructions to create their own Gmail API, not use your keys.

Run the following scripts step by step:

Extract unread emails:

python 1_gmail_unread_extract.py
Summarize emails:

python 2_email_summarizer.py
Launch dashboard:

streamlit run 3_dashboard.py
