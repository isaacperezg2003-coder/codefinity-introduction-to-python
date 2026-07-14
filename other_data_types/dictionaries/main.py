grocery_inventory = {
    "Milk": (113, "Diary"),
    "Eggs": (116, "Diary"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce"),
}

bread_details = grocery_inventory.get("Bread")

grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies: ", grocery_inventory)

grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs: ", grocery_inventory)

print("Details of bread: ", bread_details)