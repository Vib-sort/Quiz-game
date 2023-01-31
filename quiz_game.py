print("Hi ! Welcome to my Computer Quiz!")
playing =input("Do you want to play ? ")

if playing.lower() != "yes":
    exit()

print("Okay! Lets play 😊😊 ")
score=0

answer=input("what does CPU stand for? " )
if answer.lower() =="central processing unit":
    print("Correct !😉")
    score+=1
else:
    print("Incorrect! 🙁")

answer=input("what does ROM stand for? " )
if answer.lower() =="read only memory":
    print("Correct !😉")
    score+=1
else:
    print("Incorrect! 🙁")

answer=input("what does RAM stand for? " )
if answer.lower() =="random access memoryt":
    print("Correct !😉")    
    score+=1
else:
    print("Incorrect! 🙁")

answer=input("what is the full form of Wifi ? " )
if answer.lower() =="Wireless fidelity":
    print("Correct !😉")    
    score+=1
else:
    print("Incorrect! 🙁")

answer=input("what does PSU stand for? " )
if answer.lower() =="Power supply":
    print("Correct !😉")    
    score+=1
else:
    print("Incorrect! 🙁")

print("You got " + str(score)+ " questions correct")
print("You got "+ str((score/5)*100)+" % ")







