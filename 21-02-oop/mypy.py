class listop():
    list=[]
    def __init__(self):
        self.list=[]
    
    def add_element(self,name,age):
        self.list.append([name,age])
    
    def update_element(self,updateindex,name,age):
        self.updateindex=updateindex
        self.name=name
        self.age=age
        self.list[self.updateindex]=[self.name,self.age]
        
    def print_list(self) :
            return self.list   

obj=listop()
#print (obj.print_list())
obj.add_element("dheepa",21)
obj.add_element("sam",22)
obj.add_element("mahi",20)
obj.add_element("monisha",23)
obj.add_element("venki",22)
obj.add_element("sumaiya",20)
print (obj.print_list())

obj.update_element(1,"getu",20)
print (obj.print_list())