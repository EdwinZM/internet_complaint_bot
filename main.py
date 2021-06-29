from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_UP = 10
PROMISED_DOWN = 100
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if bot.down < PROMISED_DOWN and bot.up < PROMISED_UP:
    bot.tweet_at_provider()

bot.driver.quit()