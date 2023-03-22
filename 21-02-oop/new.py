class list_operation():
    l1=[]
    def _init_(self):
        self.l1=[]
        
    def add_element(self,num,name):
        self.l1.append([num,name])

    def remove_element(self,index):
        self.index=index
        if index<len(self.l1):
            self.l1.pop(self.index)
        else:
            print("index value out of range")
    
    def update_element(self,updateindex,num1,name1):
        self.updateindex=updateindex
        self.num1=num1
        self.name1=name1
        self.l1[self.updateindex]=[self.num1,self.name1]

    def remove_last(self):
        self.l1.pop()
    
    def length(self):
        print(len(self.l1))

                 
    def print_list(self) :
        return self.l1   

   
    
obj = list_operation()
print (obj.print_list())
obj.add_element(1,"dheepika")
obj.add_element(2,"sam")
obj.add_element(3,"anu")
print (obj.print_list())

obj.remove_element(1)
print(obj.print_list())
obj.update_element(1,2,"venk")
print(obj.print_list())
obj.remove_last()
print(obj.print_list())
obj.length()