import os
from pathlib import Path
from dotenv import load_dotenv
from woocommerce import API

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

url = os.getenv("URL")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

if not all([url, consumer_key, consumer_secret]):
    raise ValueError(
        "Faltan variables en .env: URL, CONSUMER_KEY y/o CONSUMER_SECRET"
    )

wcapi = API(
    url = url,
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    version="wc/v3",
    timeout=20
)