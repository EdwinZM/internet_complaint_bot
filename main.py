from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_UP = None # YOUR PROMISED DOWNLOAD SPEED
PROMISED_DOWN = None # YOUR PROMISED UPLOAD SPEED
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_USERNAME = "YOUR USERNAME"
TWITTER_PASSWORD = "YOUR PASSWORD"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if bot.down < PROMISED_DOWN and bot.up < PROMISED_UP:
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, TWITTER_USERNAME, u=PROMISED_UP, d=PROMISED_DOWN)

# bot.driver.quit()