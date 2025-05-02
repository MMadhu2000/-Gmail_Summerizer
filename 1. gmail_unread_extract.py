from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import email
import json

def extract_unread_emails():
    SCOPES = ['gmail.readonly']#path
    flow = InstalledAppFlow.from_client_secrets_file(
        r'credentials.json', SCOPES)#Path
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=10).execute()
    messages = results.get('messages', [])
    
    extracted_emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])
        
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        parts = payload.get('parts', [])
        body = ''
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                decoded_bytes = base64.urlsafe_b64decode(data)
                body = decoded_bytes.decode('utf-8')
                break
        
        extracted_emails.append({
            'subject': subject,
            'snippet': msg_data.get('snippet', ''),
            'body': body
        })

    with open('emails.json', 'w', encoding='utf-8') as f:
        json.dump(extracted_emails, f, ensure_ascii=False, indent=2)

    print(f"✅ Extracted {len(extracted_emails)} unread emails and saved to emails.json.")

if __name__ == "__main__":
    extract_unread_emails()
