####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

class Stack:
    def __init__(self):
        self._items = []
        
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        if not self._items:
            raise Exception("Stack is empty. Cannot pop.")
        return self._items.pop()
    
    def peek(self):
        if not self._items:
            raise Exception("Stack is empty. Cannot peek.")
        return self._items[-1]
    
    def size(self):
        return len(self._items)
    
    def is_empty(self):
        if self._items:
            return True
        return False
    

# function that reverses string using Stack class
def reverse_string(string):
    str_stack = Stack()
    for letter in string:
        str_stack.push(letter)
        
    reversed_string = ""
    while str_stack.size():
        reversed_string += str_stack.pop()
    
    return reversed_string    