class Queue:
    def __init__(self,sizeOfQueue):
        self.l=[]
        self.sizeOfQueue = sizeOfQueue

    def enqueue(self,val):
        if len(self.l) < self.sizeOfQueue:
            self.l.append(val)
        else:
            print("queue reached the size")
            
    def showQueue(self):
        return self.l
    
    def dequeue(self):
        self.l.pop(0)
        
    def peak(self):
        return self.l[-1]
    
    def isFull(self):
        if len(self.l)==self.sizeOfQueue:
            print("Queue is full")
        else:
            print("is not full")
            
    def isEmpty(self):
        if len(self.l)==0:
            print("Queue is empty")
        else:
            print("is not empty")
            
            
ob = Queue(5)
ob.enqueue(1)
print(ob.showQueue())
print(ob.showQueue())
ob.enqueue(5)
print(ob.showQueue())
ob.enqueue(7)
print(ob.showQueue())
ob.enqueue(9)
print(ob.showQueue())
ob.dequeue()
print(ob.showQueue())

print(ob.peak())