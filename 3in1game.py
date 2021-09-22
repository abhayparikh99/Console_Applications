import os,random
class kbc():
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
    def __init__(self):
        print("\t\t\t\t\t Welcome to KBC\n")
        print("\t\t\t\tPress 1 to enter or Press 2 to exit : ")
        choice = int(input("\t\t\t\t\tEnter your choice : "))

        if choice == 1:
            os.system('cls')
            name = input("Enter your name : ")
            print(f"Hello {name}, welcome to KBC")
            kbc.quiz(self)
        elif choice == 2:
            os.system('cls')
            print("Thank you!!!! Have a good day !!!!")
        else:
            print("Invalid Choice !!!!!")

    def quiz(self):
        for i in self.questions:
            print("\n",i)
            ans = input("Enter your answer : ")
            if ans == self.questions[i]:
                print("Correct Answer !!!!")
                self.score += 50
                self.rt_ans[i] = self.questions[i]
                print("Your score is ",self.score)
            else:
                print("Wrong Answer !!!!")
                print("Correct Answer is", self.questions[i])  # display corect ans
                self.score -= 20
                self.wr_ans[i] = ans                           # your ans
                print("Your score is ",self.score)
        kbc.rightwrongchoice(self)
    def rightwrongchoice(self):
        choice2 = 1
        while choice2:
            self.choice2 = int(
            input("\nPress 1 for right questions \nPress 2 for wrong questions \nPress 3 for exit \nEnter your choice :  "))
            if self.choice2 == 1:
                print("\nThe right answers you entered are :")
                for i in self.rt_ans:
                    print(i,"\nCorrect Answer is ",self.rt_ans[i],"\n")
            elif self.choice2 == 2:
                print("\nThe Wrong answers you entered are :")
                for j in self.wr_ans:
                    print(j, " = ", self.wr_ans[j],"is the wrong answer")
                    print("Correct Answer is ",self.questions[j],"\n")
            elif self.choice2 == 3:
                os.system('cls')
                print("Thank you for playing KBC!!!! Have a good day")
                break
            else:
                print("Invalid choice!!!!!")

    
class housie():
    def play_housie(self):
        main_list = []
        new_list = []
        comp = []
        user = []
        status = True
        while status:
            ticket = random.randint(1,100)
            if ticket not in main_list:
                main_list.append(ticket)
            no_of_tickets = len(main_list)
            if no_of_tickets==12:
                status=False
            else:
                status=True

        random.shuffle(main_list)
        new_list = main_list[:12]
        print("Welcome to Tambola Game!!!! Here are your tickets")
        print(str(new_list)[1:-1])
        comp = main_list[:6]                # Getting 6 tickets of computer from mainlist
        user = main_list[6:12]              # Getting 6 tickets of user from mainlist
        print("Computer's tickets remaining : ",str(comp)[1:-1])
        print("User's tickets remaining: ",str(user)[1:-1])
        # for loop for getting random draw of tickets and playing the game
        for num in range(len(new_list)):                
            print()
            int(input("Enter a number to draw ticket : "))
            num = random.choice(new_list)
            print(num)
            new_list.remove(num)
            if num in comp:
                print(f"Computer gets {num} from ticket!!!!")
                comp.remove(num)
                print("Computer's tickets remaining : ",str(comp)[1:-1])
                if comp==[]:
                    print("Congratulations Computer is the winner!!!!")
                    break
            else:
                print(f"User gets {num} from ticket!!!!")
                user.remove(num)
                print("User's tickets remaining: ",str(user)[1:-1])
                if user==[]:
                    print("Congratulations User is the winner!!!!")
                    break
class rockPaperScissor():
    def play_RPS(self):
        os.system('cls')                       # clearing screen for a better view        
        user_score = 0                         # variable to store user score
        comp_score = 0                         # variable to store computers score
        round = 0
        collections = ['r','p','s']
        print("ROCK !!!! PAPER !!!! SCISSOR".center(100))
        print("Welcome to play".center(100))
        print("Enter 'r' for 'rock' \nEnter 'p' for 'paper' \nEnter 's' for 'scissor'")

        while(round < 3):                      # while loop to play the game rounds
            user_choice = input("\nEnter your choice : ")
            comp_choice = random.choice(collections)
            print("Computer's choice is",comp_choice)
            # putting conditions of the game and adding scores to user and computer
            if user_choice!=comp_choice:
                round+=1
                if user_choice == 'r' and comp_choice == 's':
                    print("!!!! Congratulations you won !!!! Rock destroys Scissor !!!!")
                    user_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
                elif user_choice == 'r' and comp_choice == 'p': 
                    print("!!!! Computer won !!!! Paper covers Rock !!!!")
                    comp_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
                elif user_choice == 's' and comp_choice == 'p':
                    print("!!!! Congratulations you won !!!! Scissor cuts Paper !!!!")
                    user_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
                elif user_choice == 's' and comp_choice == 'r':
                    print("!!!! Computer won !!!! Rock destroys Scissor !!!!")
                    comp_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
                elif user_choice == 'p' and comp_choice == 'r':
                    print("!!!! Congratulations you won !!!! Paper covers Rock !!!!")
                    user_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
                elif user_choice == 'p' and comp_choice == 's':
                    print("!!!! Computer won !!!! Scissor cuts Paper !!!!")
                    comp_score+=1
                    print("Your score is ",user_score)
                    print("Computer's score is ",comp_score)
            else:
                print("It's a tie!!!! Try again")
        print("\n\nYour total score is : ",user_score)       # getting total user's scores
        print("Computer's total score is : ",comp_score)     # getting total computer's scores
        if user_score > comp_score:                          # declaring winner as per their total scores
            print("Congratulations you have won the game !!!!".center(100))
        else:
            print("Computer has won the game !!!!".center(100))
print("Welcome to 3 in 1 game".center(100))
print("Press 1 for KBC".center(100))
print("Press 2 for Housie".center(100))
print("Press 3 for Rock Paper Scissor".center(100))
choice = int(input("Enter your choice : "))
os.system('cls')
status = True
while status:
    if choice == 1:
        k=kbc()
    elif choice == 2:
        h=housie()
        h.play_housie()
    elif choice == 3:
        r=rockPaperScissor()
        r.play_RPS()
    else:
        print("Invalid choice")
        status = False