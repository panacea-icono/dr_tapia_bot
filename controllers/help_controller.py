from telegram import Update
from telegram.ext import CallbackContext

async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = "📌 *Comandos disponibles:*\n"
    help_text += "/start - Inicia el bot\n"
    help_text += "/help - Muestra esta ayuda\n"
    help_text += "/algostatus - Estado de la blockchain de Algorand\n"
    await update.message.reply_text(help_text, parse_mode="Markdown")
