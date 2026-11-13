####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:
    
    def __init__(self):
        self._items = []
        
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        if not self._items:
            raise Exception("Queue is empty. Cannot dequeue.")
        return self._items.pop(0)
    
    def peek(self):
        if not self._items:
            raise Exception("Queue is empty. Cannot peek.")
        return self._items[0]
    
    def size(self):
        return len(self._items)
    
    def is_empty(self):
        if self._items:
            return True
        return False