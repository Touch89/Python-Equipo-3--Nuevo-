from woocommerce import API
import json

wcapi = API(
  url="",
  consumer_key="",
  consumer_secret="",
  version="wc/v3",
  timeout=20
)

try:
  coupon_id = input("Coupon ID: ")
  response = wcapi.get(f"coupons/{coupon_id}")

  if response.status_code == 200:
    coupon = response.json()
    print(json.dumps(coupon, indent=1))
  else:
    print(f"Error {response.status_code}: {response.text}")

except Exception as e:
  print(f"Hubo un error de conexión: {e}")