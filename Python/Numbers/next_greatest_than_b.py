"""def next_greatest(a,b):
    l=list(str(a))
    i=len(l)-2
    while (i>=0 and l[i]>=l[i+1]):
        i=i-1
    if (i==-1):
        return -1
     
    j=len(l)-1
    while (l[i]>=l[j]):
        j=j-1

    l[i],l[j]=l[j],l[i]
    s=l[:i+1]+sorted(l[i+1:])
    next=int("".join(s))
    if (next<=b):
        return next_greatest(next,b)
    elif(next>b):
        return next
    else:
        return -1

a=int(input("a="))
b=int(input("b="))
res=next_greatest(a,b)
print(res)"""


from itertools import permutations

def next_largest_number(input1, input2):

    perm_gen = permutations(input1)
    joined_permutation = []                   
    for p in perm_gen:                 
        joined_perm = "".join(p)         
        joined_permutation.append(joined_perm)
    unique_perms = set(joined_permutation)  
    perm_list = sorted(unique_perms)
    
    for number in perm_list:
        if number > input2:
            return number
    return -1

input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

result = next_largest_number(input1, input2)
print("The next largest number is:", result)
