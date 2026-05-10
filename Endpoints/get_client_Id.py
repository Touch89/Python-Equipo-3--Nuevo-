from dependencies import wcapi
import json

try:
    customer_id = input("Ingresa el ID del cliente: ")
    response = wcapi.get(f"customers/{customer_id}")

    if response.status_code == 200:
      c = response.json()
      print(json.dumps(c, indent=2))
    else:
      print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Hubo un error de conexión: {e}")