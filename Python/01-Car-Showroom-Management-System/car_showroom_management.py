# Console Based Car Showroom Management System Using Dictionaries

showroom = {}

while True:
    print("\n========== CAR SHOWROOM MANAGEMENT SYSTEM ==========")
    print("1. Add Car")
    print("2. View All Cars")
    print("3. Search Car")
    print("4. Update Car")
    print("5. Delete Car")
    print("6. Sell Car")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    # Add Car
    if choice == "1":
        car_id = input("Enter Car ID: ")

        if car_id in showroom:
            print("Car ID already exists!")
        else:
            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            year = int(input("Enter Year: "))
            color = input("Enter Color: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            showroom[car_id] = {
                "Brand": brand,
                "Model": model,
                "Year": year,
                "Color": color,
                "Price": price,
                "Quantity": quantity
            }

            print("Car added successfully!")

    # View All Cars
    elif choice == "2":
        if not showroom:
            print("No cars available in showroom.")
        else:
            print("\n------------ Available Cars ------------")
            for car_id, details in showroom.items():
                print(f"\nCar ID : {car_id}")
                for key, value in details.items():
                    print(f"{key}: {value}")

    # Search Car by id
    elif choice == "3":
        car_id = input("Enter Car ID to search: ")

        if car_id in showroom:
            print("\nCar Found")
            print(f"Car ID: {car_id}")
            for key, value in showroom[car_id].items():
                print(f"{key}: {value}")
        else:
            print("Car not found!")

    # Update Car
    elif choice == "4":
        car_id = input("Enter Car ID to update: ")

        if car_id in showroom:
            print("Enter new details")

            showroom[car_id]["Brand"] = input("Brand: ")
            showroom[car_id]["Model"] = input("Model: ")
            showroom[car_id]["Year"] = int(input("Year: "))
            showroom[car_id]["Color"] = input("Color: ")
            showroom[car_id]["Price"] = float(input("Price: "))
            showroom[car_id]["Quantity"] = int(input("Quantity: "))

            print("Car updated successfully!")
        else:
            print("Car not found!")

    # Delete Car
    elif choice == "5":
        car_id = input("Enter Car ID to delete: ")

        if car_id in showroom:
            del showroom[car_id]
            print("Car deleted successfully!")
        else:
            print("Car not found!")

    # Sell Car
    elif choice == "6":
        car_id = input("Enter Car ID to sell: ")

        if car_id in showroom:
            if showroom[car_id]["Quantity"] > 0:
                showroom[car_id]["Quantity"] -= 1
                print("Car sold successfully!")

                if showroom[car_id]["Quantity"] == 0:
                    print("This car is now out of stock.")
            else:
                print("Car is out of stock!")
        else:
            print("Car not found!")

    # Exit
    elif choice == "7":
        print("Thank you for using Car Showroom Management System.")
        break

    else:
        print("Invalid choice! Please try again.")