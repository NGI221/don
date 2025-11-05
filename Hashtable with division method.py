TABLE_SIZE = 10
hashtable = [[] for _ in range(TABLE_SIZE)]

def hash_function(key):
    return key % TABLE_SIZE

def insert(key, value):
    idx = hash_function(key)
    
    for item in hashtable[idx]:
        if item[0] == key:
            item[1] = value
            print(f"Key {key} updated with value {value}.")
            return

    hashtable[idx].append([key, value])
    print(f"Inserted ({key}, {value}) at index {idx}.")

def search(key):
    idx = hash_function(key)
    for item in hashtable[idx]:
        if item[0] == key:
            print(f"Key {key} found with value {item[1]}.")
            return item[1]
    print(f"Key {key} not found.")
    return None

def delete(key):
    idx = hash_function(key)
    for i, item in enumerate(hashtable[idx]):
        if item[0] == key:
            del hashtable[idx][i]
            print(f"Key {key} deleted from index {idx}.")
            return
    print(f"Key {key} not found. Cannot delete.")

def display_hashtable():
    print("Current Hashtable:")
    for i, chain in enumerate(hashtable):
        print(f"Index {i}: {chain}")

while True:
    print("\nChoose operation: 1) Insert 2) Search 3) Delete 4) Display 5) Exit")
    choice = input("Enter choice number: ").strip()
    if choice == '1':
        try:
            key = int(input("Enter integer key: "))
            value = input("Enter value: ")
            insert(key, value)
        except ValueError:
            print("Key must be an integer.")
    elif choice == '2':
        try:
            key = int(input("Enter integer key to search: "))
            search(key)
        except ValueError:
            print("Key must be an integer.")
    elif choice == '3':
        try:
            key = int(input("Enter integer key to delete: "))
            delete(key)
        except ValueError:
            print("Key must be an integer.")
    elif choice == '4':
        display_hashtable()
    elif choice == '5':
        print("Exiting hashtable program.")
        break
    else:
        print("Invalid choice. Try again.")