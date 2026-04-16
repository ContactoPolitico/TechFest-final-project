import flet as ft
import requests
import json

food = {
    "Rice": {"price": 60, "stock": 10},
    "Milk": {"price": 75, "stock": 8},
    "Bread": {"price": 25, "stock": 12},
    "Eggs": {"price": 150, "stock": 7},
    "Sugar": {"price": 55, "stock": 9},
    "Coffee": {"price": 120, "stock": 5},
    "Oil": {"price": 200, "stock": 4},
    "Salt": {"price": 30, "stock": 10},
    "Flour": {"price": 65, "stock": 6},
    "Butter": {"price": 90, "stock": 5},
    "Cheese": {"price": 180, "stock": 4},
    "Ham": {"price": 140, "stock": 6},
    "Chicken": {"price": 220, "stock": 5},
    "Pasta": {"price": 70, "stock": 9},
    "Water": {"price": 20, "stock": 20},
    "Juice": {"price": 45, "stock": 10},
    "Soda": {"price": 50, "stock": 11},
    "Cookies": {"price": 60, "stock": 8},
    "Chocolate": {"price": 100, "stock": 6},
    "Yogurt": {"price": 55, "stock": 7},
    "Apples": {"price": 90, "stock": 9},
    "Bananas": {"price": 40, "stock": 12},
    "Potatoes": {"price": 50, "stock": 10},
    "Onion": {"price": 45, "stock": 8},
    "Tomato": {"price": 60, "stock": 7},
    "Sausages": {"price": 110, "stock": 5},
    "Tuna": {"price": 85, "stock": 7}
}


history = []

def main(page: ft.Page):
    page.title = "Inventory System"
    page.scroll = "auto"
    page.padding = 20
    page.window_width = 900
    page.window_height = 700

    message = ft.Text("")

    name_box = ft.TextField(label="Product name", width=200)
    price_box = ft.Text("Price: ", width=120)
    stock_box = ft.Text("Stock: ", width=120)

    move_name_box = ft.Text("Product: ", width=200)
    move_amount_box = ft.Text("Amount: ", width=120)

    delete_box = ft.TextField(label="Delete product", width=200)

    products_column = ft.Column(spacing=10)
    history_column = ft.Column(spacing=5)
    low_stock_column = ft.Column(spacing=5)

    def get_data():
        url = "https://dummyjson.com/products/category/groceries"
        response = requests.get(url)
        return response.json()

    def show_message(text, color="green"):
        message.value = text
        message.color = color
        page.update()

        data = get_data()
        print(json.dumps(data, indent=4))

        page.update()

    page.add(
        message,
        name_box,
        price_box,
        stock_box,
        move_name_box,
        move_amount_box,
        delete_box,
        history_column,
        low_stock_column,
        products_column
    )

ft.app(target=main)
