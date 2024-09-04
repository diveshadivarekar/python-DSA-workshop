class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def __str__(self):
        return str(self.items)
        

if __name__ == '__main__':
    q = Queue()
    
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    
    print("Queue items are: ", q )
    
    print(q.pop())
    
    print("Queue items are: ", q )
    