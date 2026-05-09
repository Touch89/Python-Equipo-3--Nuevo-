from woocommerce import API

wcapi = API(
    url="http://localhost:8080",
    consumer_key="ck_60afc1def93687705868d1dcae2f4448d9719355",
    consumer_secret="cs_fbf5b942b4445ebf0340a17384bb5e934a3f2c12",
    version="wc/v3",
    timeout=20
)

try:
    customer_id = input("Ingresa el ID del cliente: ")
    response = wcapi.get(f"customers/{customer_id}")

    if response.status_code == 200:
      c = response.json()
      nombre = c.get("first_name", "") + " " + c.get("last_name", "")
      print(f"ID: {c['id']} | Nombre: {nombre.strip()} | Email: {c.get('email', '')}")
    else:
      print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Hubo un error de conexión: {e}")