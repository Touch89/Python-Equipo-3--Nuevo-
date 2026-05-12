from Endpoints.dependencies import wcapi
import xmlrpc.client

url = "http://localhost:8069"
db = "db-examen"
username = "emicamposdaguer@gmail.com"
api_key = "4a0da3d342feb4abe6b06821d8b375cc7b6fea74"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, api_key, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

clientes_odoo = models.execute_kw(
    db,
    uid,
    api_key,
    'res.partner',
    'search_read',
    [[['customer_rank', '>', 0]]],
    {
        'fields': [
            'id',
            'name',
            'email',
            'phone',
            'street',
            'city',
            'country_id'
        ]
    }
)

print(f"\nSe encontraron: {len(clientes_odoo)} clientes en Odoo\n")

for cliente in clientes_odoo:
    try:
        def a_texto(valor):
            if valor in (None, False):
                return ""
            return str(valor).strip()

        nombre = cliente.get('name', '')
        email = a_texto(cliente.get('email', ''))
        telefono = a_texto(cliente.get('phone', ''))
        calle = a_texto(cliente.get('street', ''))
        ciudad = a_texto(cliente.get('city', ''))

        if not email:
            print(f"Cliente sin email omitido: {nombre}")
            continue

        response = wcapi.get(
            "customers",
            params={"email": email}
        )

        if response.status_code != 200:
            print(f"Error consultando WooCommerce: {response.text}")
            continue

        clientes_existentes = response.json()

        if clientes_existentes:
            print(f"El cliente ya existe: {email}")
            continue

        partes_nombre = nombre.split()
        first_name = partes_nombre[0] if len(partes_nombre) > 0 else ""
        last_name = " ".join(partes_nombre[1:]) if len(partes_nombre) > 1 else ""
        country = "MX"

        if cliente.get('country_id'):
            country = "MX"

        username_wc = email.split('@')[0]

        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "username": username_wc,

            "billing": {
                "first_name": first_name,
                "last_name": last_name,
                "address_1": calle,
                "city": ciudad,
                "country": country,
                "email": email,
                "phone": telefono
            },

            "shipping": {
                "first_name": first_name,
                "last_name": last_name,
                "address_1": calle,
                "city": ciudad,
                "country": country
            }
        }

        crear_cliente = wcapi.post("customers", data)

        if crear_cliente.status_code in [200, 201]:
            cliente_creado = crear_cliente.json()
            print(
                f"Cliente creado correctamente: "
                f"{cliente_creado['id']} | {email}"
            )

        else:
            print(
                f"Error creando cliente {email}: "
                f"{crear_cliente.text}"
            )

    except Exception as e:
        print(f"Error procesando cliente: {e}")

print("\n- Sincronización finalizada -\n")