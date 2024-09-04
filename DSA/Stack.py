class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def __str__(self):
        return str(self.items)
    
    
#main code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print('stack items are : ', s)
    print(s.pop())
    print(s.peek())

    print('stack items are : ', s)