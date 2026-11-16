#This program should simulate how a shpping cart works

cart = {
    
}
def add_to_cart():
    item = input("Add item to cart :")
    cart.append(item)
    print(f"{item} added to cart successfully, updated cart: {cart}" )

def view_cart():
    if cart:
        print(f"your cart has:")
        for i, item in enumerate(cart, 1):
            print(i, item)

    else:
        print("cart is empty")

def remove_item():
    item = input('Enter item to remove :')
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart successfully. updated cart: {cart}")
    elif cart ==[]:
        print("cart not found in cart")
    else:
         print(f"{item} not found in cart")

def clear_cart():
    cart.clear()
    print('cart cleared successfully')
    print("cart is now empty")

while True:
    print("\n--- CART MENU ---")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Clear cart")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_to_cart()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        clear_cart()
    elif choice == "5":
        print("Bye! 🛒")
        break
    else:
        print("Invalid option, try again.")