#This code creates a ShoppingList class allowing a customer to view available items, add items to the list, remove items from the list, view available items, and view the added items. The customer interacts with the shopping list by selecting options from the menu displayed. 

class ShoppingList:
    def __init__(self):
        self.available_items = ["Apple", "Banana", "Milk", "Bread", "Eggs"]
        self.added_items = []

    def view_available_items(self):
        print("Available items:")
        for index, item in enumerate(self.available_items, start=1):
            print(f"{index}. {item}")

    def add_item(self, item):
        if item in self.available_items:
            self.added_items.append(item)
            print(f"{item} added to the list.")
        else:
            print(f"{item} is not available in the store.")

    def remove_item(self, item):
        if item in self.added_items:
            self.added_items.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} is not in the list.")

    def view_added_items(self):
        print("Items added to the list:")
        for index, item in enumerate(self.added_items, start=1):
            print(f"{index}. {item}")

# Example Usage:
shopping = ShoppingList()

print("Welcome to the shopping list!")
shopping.view_available_items()

while True:
    print("\nMenu:")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. View available items")
    print("4. View added items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        shopping.view_available_items()
        item_choice = int(input("Enter the number of the item to add: "))
        selected_item = shopping.available_items[item_choice - 1]
        shopping.add_item(selected_item)
    elif choice == '2':
        shopping.view_added_items()
        if shopping.added_items:
            item_choice = int(input("Enter the number of the item to remove: "))
            selected_item = shopping.added_items[item_choice - 1]
            shopping.remove_item(selected_item)
        else:
            print("No items added yet.")
    elif choice == '3':
        shopping.view_available_items()
    elif choice == '4':
        shopping.view_added_items()
    elif choice == '5':
        print("Thank you for using the shopping list. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
