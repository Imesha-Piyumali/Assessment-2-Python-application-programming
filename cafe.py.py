
# Student: Imesha Piyumali, ID: u3305049, Date: 17.09.2025

# Case Study 1 — Campus Cafe Checkout

#Main Menu
MENU = {
    "coffee": (3.50, "drink"),
    "tea": (2.50, "drink"),
    "muffin": (4.00, "food"),
    "sandwich": (6.50, "food"),
    "juice": (3.00, "drink"),
    "cookie": (2.00, "food"),
}

TAX_RATE = 0.10
STUDENT_DISCOUNT = 0.05
MEAL_DEAL_DISCOUNT = 1.00  # food+drink present- If $1 off.

#Show menu
def show_menu():
    print("\n--- Menu ---")
    for item, (price, category) in MENU.items():
        print(f"{item.capitalize():10s} ${price:.2f} ({category})")

#Add items to the cart
def add_item(cart):
    show_menu()
    choice = input("Enter item name (or 'back'): ").lower()
    if choice in MENU:
        qty = int(input("Enter quantity: "))
        cart.append((choice, qty))
        print(f"Added {qty}x {choice}")
    elif choice != "back":
        print("Item not found.")

#View cart details
def view_cart(cart):
    if not cart:
        print("\nCart is Empty!")
        return
    print("\n--- Cart ---")
    for item, qty in cart:
        price, _ = MENU[item]
        print(f"{qty}x {item.capitalize()} = ${price*qty:.2f}")
    categories = {MENU[item][1] for item, _ in cart}
    print("Categories in the Cart:", categories)

#checkout the cart
def checkout(cart):
    if not cart:
        print("Cart is Empty.")
        return
    print("\n--- Receipt ---")
    subtotal = 0
    categories = set()
    for item, qty in cart:
        price, category = MENU[item]
        subtotal += price * qty
        categories.add(category)
        print(f"{qty}x {item.capitalize():10s} = ${price*qty:.2f}")
    if "food" in categories and "drink" in categories:
        print(f"Meal deal: -${MEAL_DEAL_DISCOUNT:.2f}")
        subtotal -= MEAL_DEAL_DISCOUNT
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    if input("Are you a student (y/n)? ").lower() == "y":
        discount = total * STUDENT_DISCOUNT
        total -= discount
        print(f"Student Discount!!: -${discount:.2f}")
    print(f"Total: ${total:.2f}")
    cart.clear()

#main
def main():
    cart = []
    while True:
        print("\n--- Main Menu ---")
        print("1. Show menu")
        print("2. Add item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choice: ")
        if choice == "1":
            show_menu()
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid an option!")

if __name__ == "__main__":
    main()
