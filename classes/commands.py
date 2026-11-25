import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from vendor.open_meteo import WebApi as WeatherApi


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
                                        "/help - write this message.\n"
                                        "/weather [location] - get detailed weather report in specifiect city or")

class Echo:
    async def echo(update : Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Recieve some text.")
        await update.message.reply_text(f"reply: {update.message.text}")

class Weather:
    @staticmethod
    def _cardinal_direction(degrees: float) -> str:
        directions = ("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                      "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW")
        index = round(degrees / 22.5) % len(directions)
        return directions[index]

    async def getWeather(update : Update, context : ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Recieve weather command.")
        city = " ".join(context.args)
        resp = WeatherApi.apiCall(city)
        if resp:
            current = resp.Current()
            temperature = current.Variables(0).Value()
            humidity = current.Variables(1).Value()
            cloud_cover = current.Variables(2).Value()
            wind_speed = current.Variables(3).Value()
            wind_direction = current.Variables(4).Value()
            visibility = current.Variables(5).Value()

            await update.message.reply_text(f"Current weather in {city}:\n"
                                            f"Temperature: {temperature:.1f} C\n"
                                            f"Humidity: {humidity:.0f}%\n"
                                            f"Cloud cover: {cloud_cover:.0f}%\n"
                                            f"Wind speed: {wind_speed:.1f} km/h\n"
                                            f"Wind direction: {wind_direction:.0f}\u00b0"
                                            f"({Weather._cardinal_direction(wind_direction)})\n"
                                            f"Visibility: {visibility / 1000:.1f} km")
        else:
            logger.info(f"Received unknown location: {city}")
            await update.message.reply_text("Unknown city or location.")
        