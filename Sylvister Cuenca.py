records = {}


while True:
    choice = input('Enter["add" to add data, "Del" to delete data, "End" to exit]: ')
    
    if choice == 'add':
        key = input("Enter Key:")
        value = input("Enter Value:")
        
        records[key] = value
        
        print()
        print(f"Added: {key}: {value}")
        print()
        print()
    
    
    elif choice == 'del':
        key = input("Enter key to delete: ")
        if key in records:
            del records[key]
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
print("Final records:", records)
