class Item:
    def __init__(self, item_id, name, description, price):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("The item ID must be a positive number.")
        if not name.strip():
            raise ValueError("The name cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("The price must be a non-negative number.")

        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"

class ItemManagement:
    def __init__(self):
        self.items = []

    def create_item(self):
        try:
            item_id = int(input("Enter Item ID: "))
            name = input("Enter Item Name: ").strip()
            description = input("Enter Item Description: ").strip()
            price = float(input("Enter Item Price: "))
            new_item = Item(item_id, name, description, price)
            self.items.append(new_item)
            print("Item has been created.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items:
                print(item)

    def update_item(self):
        try:
            item_id = int(input("Enter the Item ID to update: "))
            for item in self.items:
                if item.item_id == item_id:
                    name = input("Enter new Item Name: ").strip()
                    description = input("Enter new Item Description: ").strip()
                    price = float(input("Enter new Item Price: "))
                    item.name = name if name else item.name
                    item.description = description if description else item.description
                    item.price = price
                    print("Item updated successfully!")
                    return
            print("Item not found.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def delete_item(self):
        try:
            item_id = int(input("Enter the Item ID to delete: "))
            for item in self.items:
                if item.item_id == item_id:
                    self.items.remove(item)
                    print("Item deleted successfully!")
                    return
            print("Item not found.")
        except ValueError as ve:
            print(f"Error: {ve}")



def main():
    manager = ItemManagement()

    while True:
        print("\nMain Menu:")
        print("1. Create ")
        print("2. Read ")
        print("3. Update ")
        print("4. Delete ")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            manager.create_item()
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            print("Thank you for using our app!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
