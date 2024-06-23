print('''
 Car Game:
      Enter start to start the car.
      Enter stop to stop the car.
      Enter quit to quit the game    
 ''')
comm=""
prev=""
carstart=False
while True:
    comm=input("Enter your desired command>> ")
    if comm==prev:
       if comm.lower()=="start":
          print("Car already started")
       elif comm.lower()=="stop":
          print("Car already stopped")
       else :
          print("Sorry, can't understand what to do.")
    else:
        if comm.lower()=="start":
           print("Car started")
        elif comm.lower()=="stop":
           if carstart==True:
              print("Car stopped")
           else : 
               print("First start the car")
        elif comm.lower()=="quit":
           print("Quit")
           break
        else :
         print("Sorry, can't understand what to do.")
    if comm.lower()=="start":
       carstart=True
    else :
       carstart=False
    prev=comm