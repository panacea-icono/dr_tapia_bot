import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import openai
from algosdk.v2client import algod
from controllers.start_controller import start
from controllers.message_controller import handle_message
from controllers.algorand_controller import algorand_status

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ALGOD_TOKEN = os.getenv("ALGOD_TOKEN")
ALGOD_ADDRESS = os.getenv("ALGOD_ADDRESS")

# Configurar Algorand
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

# Configurar OpenAI
openai.api_key = OPENAI_API_KEY

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurar el bot
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("algostatus", algorand_status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
from controllers.help_controller import help_command
