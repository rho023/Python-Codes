n = int(input("Enter till which you want table: "))
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i} X {j} = {j*i}")
    print()