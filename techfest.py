comida = {
    "Arroz": 60,
    "Leche": 75,
    "Pan": 25,
    "Huevos": 150,
    "Azucar": 55,
    "Cafe": 120,
    "Aceite": 200,
    "Sal": 30,
    "Harina": 65,
    "Mantequilla": 90,
    "Queso": 180,
    "Jamon": 140,
    "Pollo": 220,
    "Carne de res": 300,
    "Pasta": 70,
    "Salsa de tomate": 85,
    "Mayonesa": 95,
    "Ketchup": 80,
    "Refresco": 50,
    "Agua": 20,
    "Jugo": 45,
    "Cereal": 160,
    "Galletas": 60,
    "Chocolate": 100,
    "Helado": 130,
    "Yogurt": 55,
    "Manzanas": 90,
    "Bananas": 40,
    "Naranjas": 70,
    "Papas": 50,
    "Cebolla": 45,
    "Ajo": 35,
    "Refresco": 30
    "Lechuga": 35,
    "Tomate": 60,
    "Pepino": 40,
    "Zanahoria": 30,
    "Brocoli": 80,
    "Coliflor": 85,
    "Berenjena": 75,
    "Pimientos": 90,
    "Maiz": 50,
    "Avena": 65,
    "Granola": 120,
    "Miel": 150,
    "Té": 70,
    "Leche condensada": 95,
    "Leche evaporada": 90,
    "Pan integral": 45,
    "Pan de molde": 50,
    "Croissant": 80,
    "Donas": 70,
    "Pastel": 200,
    "Pizza congelada": 180,
    "Hamburguesas": 160,
    "Salchichas": 110,
    "Tocino": 140,
    "Pescado": 250,
    "Camarones": 350,
    "Atun en lata": 85,
    "Sardinas": 70,
    "Frijoles": 60,
    "Lentejas": 65,
    "Garbanzos": 70,
    "Aceitunas": 95,
    "Vinagre": 50,
    "Mostaza": 60,
    "Salsa BBQ": 100,
    "Jarabe": 110,
    "Helado premium": 200,
    "Batidos": 90,
    "Agua con gas": 35,
    "Bebida energetica": 120,
    "Café instantaneo": 130,
    "Azucar morena": 60,
    "Harina de maiz": 55,
    "Harina integral": 75,
    "Quinoa": 180,
    "Almendras": 220,
    "Mani": 90,
    "Pasas": 80,
    "Ciruelas": 95,
    "Uvas": 120
}

carrito = {}

def mostrar_productos():
    print("------Productos del Supermercado------")
    for producto, precio in comida.items():
        print(f"{producto}: RD${precio}")
def comprar_producto():
    producto = input("Que producto quieres comprar?: ")
    if producto in comida:
        cantidad = int(input("Cantidad: "))
        carrito[producto] = carrito.get(producto, 0) + cantidad
        print(f"Agregaste {cantidad} {producto}(s) al carrito")
    else:
        print("Producto no existe")



