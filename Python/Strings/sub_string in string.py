def s(in1,in2):
    a=len(in1)
    b=len(in2)
    for i in range (a-b+1):
        if in1[i:i+b]==in2:
            return "true"
    return "empty"
    
in1=input("enter a string:")
in2=input("enter a string:")
res=s(in1,in2)
print(res)