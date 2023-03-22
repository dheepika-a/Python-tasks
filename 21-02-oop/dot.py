class Stack:
    def __init__(self,sizeOfStack):
        self.stack=[]
        self.sizeOfStack=sizeOfStack
    def push(self,val):
        if not self.isFull():
            self.stack.insert(0,val)
        else:
            print("stack is full")
    def show(self):
        return self.stack
    def Pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            self.stack.pop(0)
    def isEmpty(self):
        if len(self.stack)==0:
            return True
    def isFull(self):
        if len(self.stack)==self.sizeOfStack:
            return True
    def peak(self):
        return self.stack[-1]
ob=Stack(5)
ob.push(1)
print("this is current",ob)
print(ob.show())
ob.push(5)
print(ob.show())
ob.Pop()
print(ob.show())



