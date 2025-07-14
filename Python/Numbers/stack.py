class stack1:
    def __init__(self):
        self.stack1=[]
        
    def push(self,data):
        self.stack1.append(data)
        
    def pop(self):
        if(len(self.stack1)==0):
            print( "is empty stac")
        else:
            return self.stack1.pop()
            
    def insert(self, index, data):
        if index < 0 or index > len(self.stack1):
            return "Index out of range"
        self.stack1.insert(index, data)

    def delete(self, index):
        if index < 0 or index >= len(self.stack1):
            return "Index out of range"
        return self.stack1.pop(index)

    def extend(self, iterable):
        self.stack1.extend(iterable)

    def __str__(self):
        return str(self.stack1)
        
s=stack1()
s.push(11)
s.push(22)
s.push(55)
print(s)
s.insert(1, 3)
print(s)

s.delete(2)  
print(s)  


s.extend([7, 8, 9])  
print(s)  
s.push(19)
print(s)