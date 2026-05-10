from dependencies import wcapi

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