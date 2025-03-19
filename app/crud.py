# app/crud.py

def get_item(items: dict, item_id: str):
    if item_id not in items:
        raise KeyError(f"Item with ID '{item_id}' not found.")
    return items[item_id]

def get_all_items(items: dict):
    return list(items.values())

def get_last_item(items: dict):
    if not items:
        raise ValueError("No items available.")
    last_key = list(items.keys())[-1]
    return items[last_key]

def get_item_with_id(items: dict, item_id: str):
    return get_item(items, item_id)

def create_item(items: dict, item_id: str, item_data: dict):
    if item_id in items:
        raise ValueError(f"Item with ID '{item_id}' already exists.")
    items[item_id] = item_data

def update_item(items: dict, item_id: str, updated_data: dict):
    if item_id not in items:
        raise KeyError(f"Item with ID '{item_id}' not found.")
    items[item_id].update(updated_data)

def delete_item(items: dict, item_id: str):
    if item_id not in items:
        raise KeyError(f"Item with ID '{item_id}' not found.")
    del items[item_id]

def find_item_by_id(items: dict, item_id: str):
    return items.get(item_id, None)

def find_index_of_item(items: dict, item_id: str):
    keys = list(items.keys())
    if item_id not in keys:
        raise KeyError(f"Item with ID '{item_id}' not found.")
    return keys.index(item_id)

