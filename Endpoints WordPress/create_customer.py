from woocommerce import API

wcapi = API(
    url="http://localhost:8080",
    consumer_key="ck_6ca7ce3cfe2e00e29777e448b45518707b22f404",
    consumer_secret="cs_ac042df24d3e1cb6f12bda36415605c0e26502ea",
    version="wc/v3",
    timeout=20
)

try:
    data = {
        "email": "cliente@test.com",
        "first_name": "Juan",
        "last_name": "Perez",
        "username": "juanperez",

        "billing": {
            "address_1": "Calle 123",
            "city": "CDMX",
            "country": "MX"
        },

        "shipping": {
            "address_1": "Calle 123",
            "city": "CDMX",
            "country": "MX"
        }
    }

    response = wcapi.post("customers", data)

    if response.status_code in [200, 201]:
        cliente = response.json()
        print("- Cliente creado correctamente -")
        print(f"ID: {cliente['id']}")
        print(f"Nombre: {cliente['first_name']} {cliente['last_name']}")
        print(f"Email: {cliente['email']}")
    else:
        print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"Hubo un error de conexión: {e}")