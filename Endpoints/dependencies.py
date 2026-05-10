import os
from dotenv import load_dotenv
from woocommerce import API

load_dotenv()

wcapi = API(
    url = os.getenv("URL"),
    consumer_key = os.getenv("CONSUMER_KEY"),
    consumer_secret = os.getenv("CONSUMER_SECRET"),
    version="wc/v3",
    timeout=20
)