"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    """Return a new inventory with count more of item. Do not change inventory."""
    updated = dict(inventory)
    updated[item] = updated.get(item, 0) + count
    return updated


def total_items(*inventories):
    """Return how many items there are in all the inventories together."""
    return sum(total for inventory in inventories for total in inventory.values())


def running_low(inventory, limit=2):
    """Return the names of items with fewer than limit left, sorted A to Z."""
    return sorted(item for item, count in inventory.items() if count < limit)
