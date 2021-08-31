import random
import tkinter
from tkinter.constants import E, N, W
c_score = 0
p_score = 0
# dictionary to update score
update_score = {
    "rock":{"rock":1,"paper":0,"scissors":2},
    "paper":{"rock":2,"paper":1,"scissors":0},
    "scissors":{"rock":0,"paper":2,"scissors":1}
}
def display(user_choice):
    global c_score,p_score
    choices = ["rock","paper","scissors"]
    random_number = random.randint(0,2)
    c_choice = choices[random_number]
    result = update_score[user_choice][c_choice]
    player_choice.config(fg="purple",text="Player Choice : "+str(user_choice))
    comp_choice.config(fg="teal",text="Computer Choice : "+str(c_choice))
    
    if result == 2:
        p_score = p_score + 2
        player_score.config(text="Player : "+str(p_score))
        outcome.config(fg="blue",text="Outcome : Player Won")
    elif result == 1:
        p_score = p_score + 1
        c_score = c_score + 1
        player_score.config(text="Player : "+str(p_score))
        comp_score.config(text="Computer : "+str(c_score))
        outcome.config(fg="blue",text="Outcome : Draw")
    elif result == 0:
        c_score = c_score + 2
        comp_score.config(text="Computer : "+str(c_score))
        outcome.config(fg="blue",text="Outcome : Computer Won")

# Main title
game = tkinter.Tk()
game.title("Rock Paper Scissor")
game.geometry("600x200")
# variables
txt = tkinter.Label(game,text="Rock Paper Scissor",fg='red',font=('Calibri',15,'bold'))
txt.grid(row=0,column=0,padx=210,pady=10)

txt2 = tkinter.Label(game,text="Please Select an option",fg='blue', font=('Calibri',12,'bold'))
txt2.grid(row=1,column=0,padx=210,pady=10)

player_score = tkinter.Label(game,text="Player : 0",font=('Calibri',12,'bold'))
player_score.grid(row=2,sticky=W)
comp_score = tkinter.Label(game,text='Computer : 0',font=('Calibri',12,'bold'))
comp_score.grid(row=2,sticky=E)
player_choice = tkinter.Label(game,font=('Calibri',12))
player_choice.grid(row=3,sticky=W)
comp_choice = tkinter.Label(game,font=('Calibri',12))
comp_choice.grid(row=3,sticky=E)
outcome = tkinter.Label(game,font=('Calibri',12))
outcome.grid(row=3,sticky=N)
#Buttons
btn = tkinter.Button(game,text='Rock',fg='white',bg='blue',width=15,command=lambda:display("rock"))
btn.grid(row=4,sticky=W,padx=5,pady=5)
btn = tkinter.Button(game,text='Paper',fg='white',bg='blue',width=15,command=lambda:display("paper"))
btn.grid(row=4,sticky=N,pady=5)
btn = tkinter.Button(game,text='Scissors',fg='white',bg='blue',width=15,command=lambda:display("scissors"))
btn.grid(row=4,sticky=E,padx=5,pady=5)
game.mainloop()