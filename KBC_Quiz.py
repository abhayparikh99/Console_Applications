import os
os.system('cls')
score = 0
wr_ans = {}  # dictionary to store wrong ans along with questions
rt_ans = {}  # dictionary to store right ans along with questions
q1 = '''Q1. You can see me, but I weight nothing. If you put me 
    in a bucket of water I'll make it lighter. What am I ?\n
    \tA. Ballon \t\tB. Sand \n\tC. Water \t\tD. A Hole'''
q2 = '''Q2. What is something that you are forever leaving behind
    but still always have ?\n
    \tA. Smell \t\tB. Fingerprints \n\tC. Pain \t\tD. Memory'''
q3 = '''Q3. What can fly but has no wings ?\n
    \tA. Water \t\tB. Knowledge \n\tC. Time \t\tD. Stone'''
q4 = '''Q4. What are the largest ant in the world ?\n
    \tA. Giraffe \t\tB. Elephant \n\tC. Dinosaur \t\tD. Whale'''
q5 = '''Q5. Of the options below, what has four legs, one head and one foot ?\n
    \tA. An Amazonian rabbit \t\tB. A three-legged dog \n\tC. A Bed \t\t\tD. A Chair'''
q6 = '''Q6. The person who made it doesn't want it, the person who 
    paid for it doesn't need it, and the person who needs it doesn't 
    know it. What is it ?\n
    \tA. A Cake \t\tB. A Car \n\tC. A Meal \t\tD. A Coffin'''
q7 = '''Q7. What has branches, but no bark ?\n
    \tA. A Dog Pound \t\tB. A library \n\tC. A Car \t\tD. A Forest'''
q8 = '''Q8. Everybody has me but I'm impossible to lose. What am I ?\n
    \tA. Money \t\tB. Skin \n\tC. Shadow \t\tD. Hair'''
q9 = '''Q9. What is the next number in the pattern: 16,25,36,49,__ ?\n
    \tA. 54 \t\tB. 77 \n\tC. 64 \t\tD. 72'''
q10 = '''Q10. I Often run, but I don't have legs. I don't need 
    you, but you need me. What am I ?\n
    \tA. Athelete \t\tB. a Movie \n\tC. Ladder \t\tD. Water'''

questions = {q1: "d", q2: "b", q3: "c", q4: "b", q5: "c",
             q6: "d", q7: "b", q8: "c", q9: "c", q10: "d"}
print("\t\t\t\t\t Welcome to KBC\n")
print("\t\t\t\tPress 1 to enter or Press 2 to exit : ")
choice = int(input("\t\t\t\t\tEnter your choice : "))

def quiz():
    global score,rt_ans,wr_ans
    for i in questions:
        print("\n",i)
        ans = input("Enter your answer : ")
        if ans == questions[i]:
            print("Correct Answer !!!!")
            score += 50
            rt_ans[i] = questions[i]
            print("Your score is ", score)
        else:
            print("Wrong Answer !!!!")
            print("Correct Answer is", questions[i])  # display correct ans
            score -= 20
            wr_ans[i] = ans                           # your ans
            print("Your score is ", score)

def rightwrongchoice():
    global score,rt_ans,wr_ans
    choice2 = 1
    while choice2:
        choice2 = int(
            input("\nPress 1 for right questions \nPress 2 for wrong questions \nPress 3 for exit \nEnter your choice :  "))
        if choice2 == 1:
            print("\nThe right answers you entered are :")
            for i in rt_ans:
                print(i,"\nCorrect Answer is ",rt_ans[i],"\n")
        elif choice2 == 2:
            print("\nThe Wrong answers you entered are :")
            for j in wr_ans:
                print(j, " = ", wr_ans[j],"is the wrong answer")
                print("Correct Answer is ",questions[j],"\n")
        elif choice2 == 3:
            os.system('cls')
            print("Thank you for playing KBC!!!! Have a good day")
            break
        else:
            print("Invalid choice!!!!!")

if choice == 1:
    os.system('cls')
    name = input("Enter your name : ")
    print(f"Hello {name}, welcome to KBC")
    quiz()
    rightwrongchoice()
elif choice == 2:
    os.system('cls')
    print("Thank you!!!! Have a good day !!!!")
else:
    print("Invalid Choice !!!!!")