print("Welcome to the Quiz Game!")

playing = input("Do you want to play the game? ")

if playing.lower() != 'yes':
    quit() # It is an command used to stop the interpreter, mainly in interactive sessions. terminates the programm.

print("okay Let's Play :)")

score = 0

Q = "What does CPU stands for?"
print(Q)
ans = input("ans: ")

if ans.lower() == "central processing unit":
    print("Whoa! you are correct.")
    score += 1
else:
    print("Sorry, answer is Incorrect.")
    
    
    
Q = "What will be the output of 'print(upper.hello)'?"
print(Q)
ans = input("ans: ")

if ans == "HELLO":
    print("Whoa! you are correct.")
    score += 1
else:
    print("Sorry, answer is Incorrect.")
    
    
Q = "What is the data type of 'vivek'?"
print(Q)
ans = input("ans: ")

if ans.lower() == "string":
    print("Whoa! you are correct.")
    score += 1
else:
    print("Sorry, answer is Incorrect.")
    
    
Q = "Who is the most followed insta person?"
print(Q)
ans = input("ans: ")

if ans.lower() == "cristiano ronaldo":
    print("Whoa! you are correct.")
    score += 1
else:
    print("Sorry, answer is Incorrect.")
    
    
Q = "Who was the winner of '2022 fifa world cup'?"
print(Q)
ans = input("ans: ")

if ans.lower() == "argentina":
    print("Whoa! you are correct.")
    score += 1
else:
    print("Sorry, answer is Incorrect.")
    
total_score = score
print("Your total Score is -> ",total_score)


if total_score <= 5:
    print("Excellent!, you got" + str(total_score)+ "very good.")
elif total_score == 4:
    print("Nice!, you got " + str(total_score) +  "very good.")
elif (2 <= total_score <= 3 ):
    ("Try Hard next time, your score is" + str(total_score))
else:
    print("Better Luck next time"+str(total_score))