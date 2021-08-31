import random
main_list = []
new_list = []
comp = []
user = []

#while loop to get random 12 tickets

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
print(main_list)

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

    
            
