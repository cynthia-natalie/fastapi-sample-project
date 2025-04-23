import pytest

# Assuming you have a crud.py with get_item and create_item functions
from app.crud import (
    get_item,
    get_all_items,
    get_last_item,
    get_item_with_id,
    create_item,
    update_item,
    delete_item,
    find_item_by_id,
    find_index_of_item,
)

@pytest.fixture
def sample_items():
    return {
        "item1": {"name": "Item 1", "description": "First item"},
        "item2": {"name": "Item 2", "description": "Second item"},
        "item3": {"name": "Item 3", "description": "Third item"},
    }

def test_get_item(sample_items):
    item = get_item(sample_items, "item1")
    assert item["name"] == "Item 1"

def test_get_item_not_found(sample_items):
    with pytest.raises(KeyError):
        get_item(sample_items, "itemX")

def test_get_all_items(sample_items):
    all_items = get_all_items(sample_items)
    assert len(all_items) == 3

def test_get_last_item(sample_items):
    last_item = get_last_item(sample_items)
    assert last_item["name"] == "Item 3"

def test_get_last_item_empty():
    with pytest.raises(ValueError):
        get_last_item({})

def test_create_item(sample_items):
    create_item(sample_items, "item4", {"name": "Item 4", "description": "Fourth item"})
    assert "item4" in sample_items

def test_create_item_already_exists(sample_items):
    with pytest.raises(ValueError):
        create_item(sample_items, "item1", {"name": "Duplicate", "description": "Duplicate item"})

def test_update_item(sample_items):
    update_item(sample_items, "item2", {"description": "Updated description"})
    assert sample_items["item2"]["description"] == "Updated description"

def test_update_item_not_found(sample_items):
    with pytest.raises(KeyError):
        update_item(sample_items, "itemX", {"description": "New description"})

def test_delete_item(sample_items):
    delete_item(sample_items, "item1")
    assert "item1" not in sample_items

def test_delete_item_not_found(sample_items):
    with pytest.raises(KeyError):
        delete_item(sample_items, "itemX")

def test_find_item_by_id(sample_items):
    item = find_item_by_id(sample_items, "item2")
    assert item["name"] == "Item 2"

def test_find_item_by_id_not_found(sample_items):
    item = find_item_by_id(sample_items, "itemX")
    assert item is None

def test_find_index_of_item(sample_items):
    index = find_index_of_item(sample_items, "item2")
    assert index == 1

def test_find_index_of_item_not_found(sample_items):
    with pytest.raises(KeyError):
        find_index_of_item(sample_items, "itemX")

# items = {"foo": {"name": "Foo", "description": "A test item"}}

# def test_get_item():
#     item = get_item(items, "foo")
#     assert item["name"] == "Foo"
#     assert item["description"] == "A test item"

# def test_get_item_not_found():
#     with pytest.raises(KeyError):
#         get_item(items, "bar")

# def test_create_item():
#     new_item = {"name": "Bar", "description": "Another test item"}
#     create_item(items, "bar", new_item)
#     assert "bar" in items
#     assert items["bar"] == new_item

# def test_create_item_already_exists():
#     with pytest.raises(ValueError):
#         create_item(items, "foo", {"name": "Foo", "description": "Duplicate item"})
