number=input("Enter any natural number other than 1: ")
prime=[]
num=int(number)
for i in range(2,num+1):
    pri=True
    if num%i==0:
        for j in range(2,i):
            if i%j==0:
               pri=False
               break
        if pri==True:
            prime.append(i)
print("The set of prime factors for the given number is: ")
print(prime)