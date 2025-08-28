import requests
import textwrap
import os

# استخدام Secrets من GitHub Actions
TOKEN = os.environ.get("TELEGRAM_TOKEN")
chat_ids = [
    os.environ.get("CHAT_ID_1"),
    os.environ.get("CHAT_ID_2"),
    os.environ.get("CHAT_ID_3")
]

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_message(text, chat_id):
    try:
        response = requests.post(URL, data={"chat_id": chat_id, "text": text})
        if response.status_code == 200:
            print(f"تم الإرسال ✅ إلى {chat_id}")
        else:
            print(f"خطأ 🚨 في {chat_id}: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def send_long_message(text, chunk_size=3500):
    for chunk in textwrap.wrap(text, chunk_size, break_long_words=False, replace_whitespace=False):
        for chat_id in chat_ids:
            if chat_id:
                send_message(chunk, chat_id)

# رسالة تجريبية
test_message = "🟢 رسالة تجريبية: البوت شغال! ✅"

if __name__ == "__main__":
    send_long_message(test_message)
