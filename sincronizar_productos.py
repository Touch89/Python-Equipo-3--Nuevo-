from Endpoints.dependencies import wcapi
import xmlrpc.client

url = "http://localhost:8069"
db = "angeldb"
db = "EMIDB"
username = "emiliovad1205@gmail.com"
password = "admin123"
api_key = "ca0b4b32b560f3096cf1272ce474421d2ee8f713"


common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, api_key, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

try:
    productos_odoo = models.execute_kw(
        db,
        uid,
        api_key,
        'product.template',
        'search_read',
        [[]],
        {'fields': ['name', 'list_price', 'default_code']}
    )

    print(f"--- {len(productos_odoo)} Productos encontrados en Odoo ---")

    for p in productos_odoo:
        sku = p["default_code"] or ""

        if sku:
            existing = wcapi.get("products", params={"sku": sku}).json()
            if existing:
                print(f"El producto ya existe: {p['name']}")
                continue

        data = {
            "name": p["name"],
            "type": "simple",
            "regular_price": str(p["list_price"]),
            "sku": sku,
            "description": "Importado desde Odoo"
        }

        response = wcapi.post("products", data)

        if response.status_code in [200, 201]:
            print(f"Creado: {p['name']}")
        else:
            print(f"Error {p['name']}: {response.text}")

except Exception as e:
    print(f"Hubo un error de conexión: {e}")