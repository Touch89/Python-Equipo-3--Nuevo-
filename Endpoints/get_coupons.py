from dependencies import wcapi
import json

try:
    response = wcapi.get("coupons")

    if response.status_code == 200:
        coupons = response.json()
        print(json.dumps(coupons, indent=1))
    else:
        print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Hubo un error de conexión: {e}")