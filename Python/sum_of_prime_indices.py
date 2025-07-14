def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
def sum_of_prime_indices(arr,n):
    sum=0
    for i in range(2,n):
        if(isPrime(i)):
            sum=sum+arr[i]
    return sum
n=int(input()) #6
arr=list(map(int,input().split())) [:n] #3 6 3 9 4 2
v=sum_of_prime_indices(arr,n)
print(v) #14
