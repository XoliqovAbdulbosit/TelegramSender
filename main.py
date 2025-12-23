import requests
import json
import re

BOT_TOKEN = ""
FIRST_USER_ID = 998457944
MESSAGE_TEXT = """"""

def load_ids(filename="ids.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {filename}: {e}")
        return []

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(f"Sent to {chat_id}")
    else:
        print(f"Failed to send to {chat_id}: {response.text}")

def main():
    other_user_ids = load_ids()

    send_message(FIRST_USER_ID, MESSAGE_TEXT)

    confirm = input("Do you confirm sent message (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Message sending aborted.")
        return

    for user_id in other_user_ids:
        send_message(user_id, MESSAGE_TEXT)

if __name__ == "__main__":
    main()
