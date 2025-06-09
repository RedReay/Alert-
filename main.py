import os
import requests
import tweepy
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)

# Пользователи Twitter, за которыми следим
TWITTER_USERS = [
    "elonmusk", "saylor", "APompliano", "cz_binance", "justinsuntron",
    "BarrySilbert", "brian_armstrong", "jack", "VitalikButerin", "Tether_to",
    "realDonaldTrump", "balajis"
]

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_latest_tweets(username):
    user = client.get_user(username=username)
    tweets = client.get_users_tweets(id=user.data.id, max_results=5)
    return tweets.data if tweets and tweets.data else []

def main():
    for user in TWITTER_USERS:
        try:
            tweets = fetch_latest_tweets(user)
            for tweet in tweets:
                message = f"🧠 Новое сообщение от @{user}:

{tweet.text}"
                bot.send_message(chat_id=TELEGRAM_CHANNEL, text=message)
        except Exception as e:
            print(f"Ошибка при получении твитов {user}: {e}")

if __name__ == "__main__":
    main()
