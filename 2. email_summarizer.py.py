from transformers import pipeline
import json
import os

def summarize_emails():
    if not os.path.exists('emails.json'):
        print("emails.json not found. Run 1_gmail_unread_extract.py first.")
        return
    
    with open('emails.json', 'r', encoding='utf-8') as f:
        emails = json.load(f)

    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    summarized_data = []
    for email_item in emails:
        body = email_item['body'].strip()
        if not body:
            summary = "No body to summarize."
        else:
            truncated_body = body[:1000]

            summary_text = summarizer(
                truncated_body, max_length=130, min_length=30, do_sample=False
            )[0]['summary_text']
            summary = summary_text
        
        summarized_data.append({
            'subject': email_item['subject'],
            'snippet': email_item['snippet'],
            'summary': summary
        })
    
    with open('summaries.json', 'w', encoding='utf-8') as f:
        json.dump(summarized_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Summarized {len(summarized_data)} emails and saved to summaries.json.")

if __name__ == "__main__":
    summarize_emails()
