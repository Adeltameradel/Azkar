import datetime
import requests
import textwrap
import os

# استخدام Secrets من GitHub Actions
TOKEN = os.environ.get("TELEGRAM_TOKEN")
# قائمة الـ Chat IDs للجروبات المختلفة
chat_ids = [
    os.environ.get("CHAT_ID_1"),
    os.environ.get("CHAT_ID_2"),
    os.environ.get("CHAT_ID_3")
    # ممكن تضيف Chat_ID_X جديد هنا لأي جروب إضافي
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
    """يقسم النص الطويل ويرسله على عدة رسائل لكل جروب"""
    for chunk in textwrap.wrap(text, chunk_size, break_long_words=False, replace_whitespace=False):
        for chat_id in chat_ids:
            if chat_id:
                send_message(chunk, chat_id)

# 📖 أذكار الصباح
azkar_sabah = """📖 أذكار الصباح
...
(هنا كامل نص أذكار الصباح)
...
"""

# 🌙 أذكار المساء
azkar_masaa = """🌙 أذكار المساء
...
(هنا كامل نص أذكار المساء)
...
"""

# ✨ حديث قصير
hadith = """قال رسول الله ﷺ:
(احرص على ما ينفعك، واستعن بالله ولا تعجز)
رواه مسلم.
"""

if __name__ == "__main__":
    # رسالة تجريبية فورية لو شغلنا الرن يدوي
    send_long_message("🟢 رسالة تجريبية: البوت شغال! ✅")

    # بعد كده النظام الطبيعي للرسائل حسب الوقت
    hour = datetime.datetime.now().hour
    message = None

    if hour == 7:        # وقت أذكار الصباح
        message = azkar_sabah
    elif hour == 13:     # وقت الحديث
        message = hadith
    elif hour == 20:     # وقت أذكار المساء
        message = azkar_masaa

    if message:
        send_long_message(message)
    else:
        print("مش وقت الرسالة حالياً")
