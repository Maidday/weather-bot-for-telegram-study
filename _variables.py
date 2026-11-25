#AFTER FILLING IN MISSING VALUES, RENAME THIS FILE TO "variables.py" to compile

class Systemvariables:
    def __init__(self):
        self.__token = " "  #HERE GOES YOUR TELEGRAM TOKEN BOT
        self.__useragent = " " #HERE GOES YOUR USER AGENT FOR GEOPY

    def getToken(self):
        return self.__token

    def getUserAgent(self):
        return self.__useragent
    
