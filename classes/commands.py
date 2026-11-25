import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


logger = logging.getLogger(__name__)

class start:
    async def startBot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Recieve start command.")
        await update.message.reply_text("Welcome to the Weatherman bot!\n"
                                        "Lookup current weather in specified area.\n" 
                                        "Use /help to get a help on commands.")

class HelpCommand:
    async def printHelp(update : Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Recieve help command.")
        await update.message.reply_text("Weatherman Bot v0.0.1\n"
                                        "/start - start bot.\n"
                                        "/help - write this message.")

class Echo:
    async def echo(update : Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Recieve some text.")
        await update.message.reply_text(f"reply: {update.message.text}")