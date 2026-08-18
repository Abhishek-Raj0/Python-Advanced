import sys

inventory = {}
for line in sys.stdin:
    parts = line.strip().split()
    cmd = parts[0]
    # Handle add, remove, search, list
    if cmd == "add":
        item, qty = parts[1], int(parts[2])
        inventory[item] = inventory.get(item, 0) + qty

    elif cmd == "remove":
        item, qty = parts[1], int(parts[2])
        if item not in inventory:
            print("error: not found")
        elif inventory[item] < qty:
            print("error: insufficient")
        else:
            inventory[item] -= qty
            if inventory[item] == 0:
                del inventory[item]

    elif cmd == "search":
        item = parts[1]
        print(inventory.get(item, 0))

    elif cmd == "list":
        if not inventory:
            print("empty")
        else:
            for item in sorted(inventory):
                print(f"{item}: {inventory[item]}")
