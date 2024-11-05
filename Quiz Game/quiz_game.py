playing = input("Do you want to play? y/n: ").lower()
score = 0

if playing != "y":
    quit()

print("okay! lets play")

answer = input("What is CPU stands for: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is GPU stands for: ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is RAM stands for: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is ROM stands for: ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"you got {score} questions correct")
print(f"you score is {(score/4)*100}%")