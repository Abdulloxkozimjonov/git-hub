import requests

def send_message(chat_id, text):
    bot_token = "6666019423:AAEydYdtDSee9yRTck-FimWO9YY6C42ElsY"
    api_url = f"https://api.telegram.org/bot{6666019423:AAEydYdtDSee9yRTck-FimWO9YY6C42ElsY}/sendMessage"
    params = {"6255585652": chat_id, "text": text}
    response = requests.get(api_url, params=params)
    return response.json()

# Test qilish
chat_id = "6255585652"
text = "Assalomu alaykum! Bu test xabar."
send_message(chat_id, text)