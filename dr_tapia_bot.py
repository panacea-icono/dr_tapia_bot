import os
import openai
import telebot
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar claves API
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializar el bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Configurar OpenAI
openai.api_key = OPENAI_API_KEY

def get_openai_response(prompt):
    """Obtiene una respuesta de OpenAI basado en el prompt dado."""
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Eres un asistente de cirugía plástica."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al obtener respuesta: {str(e)}"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, soy el Dr. Tapia Bot. ¿En qué puedo ayudarte con cirugía plástica?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = get_openai_response(user_input)
    bot.reply_to(message, response)

if __name__ == "__main__":
    print("Bot en ejecución...")
    bot.remove_webhook()
    bot.set_webhook(url="https://tudominio.com/" + TELEGRAM_TOKEN)

# Estructura de carpetas
os.makedirs("config", exist_ok=True)
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Crear archivos base
with open("requirements.txt", "w") as f:
    f.write("python-dotenv\n")
    f.write("openai\n")
    f.write("pyTelegramBotAPI\n")

with open(".env", "w") as f:
    f.write("TELEGRAM_TOKEN=your_telegram_token_here\n")
    f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
