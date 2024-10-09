import os
import requests

lst = []
TOKEN = ""
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
current_directory = os.getcwd()


def send_photo(chat_id, photo, text):
    url = f"{BASE_URL}/sendPhoto"
    img = os.path.join(current_directory, photo)
    with open(img, "rb") as image_file:
        files = {"photo": image_file}
        data = {"chat_id": chat_id, "caption": text, "parse_mode": "Markdown"}
        requests.post(url, files=files, data=data)


def send_text(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=data)


def send_video_note(chat_id, video_note):
    url = f"{BASE_URL}/sendVideoNote"
    video = os.path.join(current_directory, video_note)
    with open(video, "rb") as video_file:
        files = {"video_note": video_file}
        data = {"chat_id": chat_id}
        requests.post(url, files=files, data=data)


def forward(chat_id):
    url = f"{BASE_URL}/forwardMessage"
    from_chat_id = 0
    message_id = 0
    data = {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_id": message_id}
    requests.post(url, data=data)


data = ""
print(len(lst))
errors = []
cnt = 0
for id in lst:
    try:
        forward(id)
        print(cnt, id)
    except Exception as e:
        print("Error:", e, cnt, id)
        errors.append(id)
    cnt += 1
print("Errors:", errors)
