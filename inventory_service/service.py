# Inventory polling service

import time

from inventory_service.warehouse import get_inventory
from inventory_service.cache import update_cache


POLL_INTERVAL = 300  # 5 minutes


def poll_warehouse():
    """
    Gets the latest inventory from the warehouse
    and updates the local cache.
    """
    inventory = get_inventory()
    update_cache(inventory)

    print("Inventory cache updated.")
    print(inventory)


def start_polling():
    """
    Continuously polls the warehouse every 5 minutes.
    """
    while True:
        poll_warehouse()

        print(f"Waiting {POLL_INTERVAL} seconds until the next poll...")
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    start_polling()