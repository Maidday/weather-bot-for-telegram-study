import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from variables import Systemvariables
from classes.commands import start, HelpCommand, Echo

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("root").setLevel(logging.INFO)
logger = logging.getLogger(__name__)

sysVars = Systemvariables()

if __name__ == "__main__":
    logger.info("Start bot")
    application = Application.builder().token(sysVars.getToken()).build()

    application.add_handler(CommandHandler("start", start.startBot))
    application.add_handler(CommandHandler("help", HelpCommand.printHelp))

    application.add_handler(MessageHandler(filters.TEXT, Echo.echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Stop bot")




