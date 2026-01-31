inventory = []

def add_medicine(name, batch, expiry, quantity):
    medicine = {
        "name": name,
        "batch": batch,
        "expiry": expiry,
        "quantity": quantity
    }
    inventory.append(medicine)

def get_inventory():
    return inventory
