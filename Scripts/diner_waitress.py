#!/usr/bin/env python3

def diner_waitress():
    # Start with an empty list for the order
    order = []

    print("Hello, I'll be your waitress. What will you have?\n")

    # Start an infinite loop to take orders
    while True:
        # Ask for a menu item
        item = input("menu item: ")

        # Check if the customer is done ordering
        if item.lower() == "that's all":
            break  # Exit the loop
        else:
            # Add the item to the order list
            order.append(item)

    # Print the completed order
    print("\nYou've ordered:")
    print(order)


# Run the function
if __name__ == "__main__":
    diner_waitress()

