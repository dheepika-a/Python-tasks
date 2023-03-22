class myclass():
    def __init__(self,sizeofqueue):
        self.list=[]
        self.siz
    def enqueue(self,val):
        self.list.append(val)
    def showqueue(self):
        print(self.list)
    
    
obj=myclass()
obj.enqueue(1)
obj.enqueue(1)
obj.enqueue(7)
obj.showqueue()