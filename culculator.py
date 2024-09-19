import json

workTables = {}

def saveWorkTables():
    # Saving the workTables with keys as strings to allow JSON serialization
    with open('workTables.json', 'w') as file:
        json.dump({f"{k[0]}-{k[1]}": v for k, v in workTables.items()}, file)
    print("Work hours have been saved.")

def loadWorkTables():
    global workTables
    try:
        with open('workTables.json', 'r') as file:
            # Load workTables and convert keys back to tuples
            loaded_data = json.load(file)
            workTables = {tuple(map(int, k.split('-'))): v for k, v in loaded_data.items()}
            
            # Check if the loaded data is an empty dictionary
            if not workTables:
                print("The file is empty. No work hours loaded.")
            else:
                print("Work hours have been loaded.")
    except FileNotFoundError:
        print("No saved data found.")
    except json.JSONDecodeError:
        # If the file is not in a valid JSON format for some reason
        print("The file is literally empty")
        workTables = {}

def inputNums():
    month = int(input("Enter the month (int[1-12]): "))
    day = int(input("Enter the day (int[1-31]): "))
    workHours = float(input("Enter the work hours (float): "))

    workTables[(month, day)] = workHours

def checkWorkHours():
    # Display header
    print("The work hours of this month are:")
    print(f"{'Month':<10} {'Day':<10} {'Work Hours':<15}")
    print("-" * 35)  

    for date, hours in workTables.items():
        print(f"{date[0]:<10} {date[1]:<10} {hours:<15.2f}")

    # Display total work hours
    total_hours = sum(workTables.values())
    print("-" * 35)
    print(f"{'Total':<20} {total_hours:<15.2f}")

def resetWorkHours():
    workTables.clear()
    print("Work hours have been reset.")

# Load saved data at the start of the program
loadWorkTables()

while True:
    print("\n1. Input work hours")
    print("2. Check work hours")
    print("3. Reset work hours")
    print("4. Exit")
    choice = input("Please choose: ")
    print("--------------------")

    if choice == "1":
        inputNums()
    elif choice == "2":
        checkWorkHours()
    elif choice == "3":
        resetWorkHours()
    elif choice == "4":
        # Save data before exiting
        saveWorkTables()
        break
    else:
        print("Invalid choice, please try again.")
    print("--------------------")
