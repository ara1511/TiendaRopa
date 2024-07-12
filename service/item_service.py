from abc import ABC, abstractmethod

class ItemService(ABC):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_all_items(self):
        return self._items

    def get_item_by_id(self, id):
        for item in self._items:
            if item.id == id:
                return item
        return None
