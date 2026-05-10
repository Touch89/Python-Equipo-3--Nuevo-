from dependencies import wcapi


def obtener_clientes(per_page=50, max_paginas=20):
    clientes = []

    for pagina in range(1, max_paginas + 1):
        response = wcapi.get(
            "customers",
            params={"per_page": per_page, "page": pagina}
        )

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return []

        data = response.json()

        if not isinstance(data, list) or not data:
            break

        clientes.extend(data)

        if len(data) < per_page:
            break

    return clientes


try:
    clientes = obtener_clientes()

    if not clientes:
        print("No se encontraron clientes en WooCommerce")
    else:
        print(f"--- Se encontraron {len(clientes)} clientes ---")

        for c in clientes:
            nombre = f"{c.get('first_name', '')} {c.get('last_name', '')}".strip()
            if not nombre:
                nombre = c.get("username", "Sin nombre")

            print(
                f"ID: {c.get('id')} | "
                f"Nombre: {nombre} | "
                f"Email: {c.get('email', '')} | "
                f"Usuario: {c.get('username', '')}"
            )

except Exception as e:
    print(f"Hubo un error de conexión: {e}")
