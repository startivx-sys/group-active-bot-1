import telebot
import time
import os
from threading import Thread
from flask import Flask

# Render ko "alive" rakhne ke liye server
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Aapki details
TOKEN = "8206426384:AAF-HGUulw0e02TSbH9ovxWgL0wmSkWkFR8"
CHAT_ID = -1003391238850  # Telegram group IDs hamesha -100 se shuru hoti hain

bot = telebot.TeleBot(TOKEN)

# Aapka Message
MESSAGE_TEXT = """
*Join our Telegram channel for:*

✅ Real work-from-home jobs
✅ Part-time & freelancing work
✅ Daily earning updates
✅ No investment opportunities
✅ Beginner-friendly guidance

👉 *Join Now and Start Earning Today!*
Channel : @onlineworkersmedia
"""

def send_auto_msg():
    while True:
        try:
            bot.send_message(CHAT_ID, MESSAGE_TEXT, parse_mode="Markdown")
            print("Message successfully sent!")
            # 300 seconds = 5 minutes
            time.sleep(300) 
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(30) # Error aane par 30 sec wait karega

if __name__ == "__main__":
    keep_alive()
    print("Bot active ho gaya hai...")
    send_auto_msg()
