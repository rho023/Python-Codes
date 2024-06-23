numbers=[4,67,84,29,12,27,48,43,90]
for num in numbers:
    i=0
    largest=True
    while i<len(numbers) and largest==True:
          if num>=numbers[i]:
             largest=True
          else :
              largest=False
          i=i+1    
    if largest==True:
        print(str(num) +" is the largest number")    
        break    