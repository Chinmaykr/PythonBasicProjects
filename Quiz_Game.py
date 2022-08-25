from tkinter.messagebox import YES


print("Welcome to my computer quiz!")

playing = input("Do you wantr to play ")

if playing.lower() != "yes":
     quit()
    
print("Okay! Let's Play:")
score =0   

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    score -= 1


answer = input("what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    score -= 1


answer = input("what does RAM stand for?")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    score -= 1


answer = input("what does ROM stand for?")
if answer.lower() == "random operating memory":
    print('correct!')
    score += 1
else:
    print('incorrect!')
    score -= 1
    
    
print ('your score is ' , str(score)  )
print ('your got ' + str(score/4*100) + '%.')