data = {}


while True:
    choice = input('Enter["add" to add data, "Del" to delete data, "End" to exit]: ')
    
    if choice == 'add':
        key = input("Enter Key:")
        value = input("Enter Value:")
        
        data[key] = value
        
        print()
        print(f"Added: {key}: {value}")
        print()
        print()
    
    
    elif choice == 'del':
        key = input("Enter key to delete: ")
        if key in data:
            del data[key]
            print()
            print(f"Deleted: {key}")
            print()
            print()
        else:
            print("Key not found in records.")    
    
    elif choice == 'end':
        break
    
    else:
        print("Invalid choice. Please try again")


print()
print()
print("Final records:", data)
print()
print("THANK YOU")
