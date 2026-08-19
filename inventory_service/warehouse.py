# Simulated warehouse API

warehouse_inventory = {
    "laptop": 15,
    "phone": 8,
    "keyboard": 0,
    "mouse": 25
}


def get_inventory():
    """
    Simulates getting the latest inventory
    from a warehouse API.
    """
    return warehouse_inventory.copy()
if __name__ == "__main__":
    print(get_inventory())