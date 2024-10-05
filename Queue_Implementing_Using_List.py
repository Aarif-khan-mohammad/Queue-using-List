class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)
        
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")
            

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    
    def size(self):
        return len(self.items)
    
    
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Front Value : ",q1.get_front())
print("Rear Value : ",q1.get_rear())
print("Size of Queue : ",q1.size())
q1.dequeue()
print("Front Value : ",q1.get_front())
print("Rear Value : ",q1.get_rear())
print("Size of Queue : ",q1.size())
    