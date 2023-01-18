#Rock Paper Scissors Game

import random

def game(comp, you): #making game function
    if comp == you: #if inputs are same
        return None
    elif comp=='R': #comp choosed rock
        if you=='P':
            return True
        elif you == 'S':
            return False
    elif comp=='P': #comp choosed paper
        if you=='R':
            return False
        elif you == 'S':
            return True
    elif comp=='S': #comp choosed scissors
        if you=='P':
            return False
        elif you == 'R':
            return True
    

print("Computer Turn: Rock(R) Paper(P) or Scissors(S) ?")
rand_no = random.randint(1,3)  #comp choosing randomly
if rand_no==1:
    comp = 'R'
elif rand_no==2:
    comp = 'P'
elif rand_no==3:
    comp = 'S'
you = input("Your Turn: Rock(R) Paper(P) or Scissors(S) ?") #taking input
you = you.capitalize() #capitalising it if it's not to match the code

# execution 
print(f"Computer choosed {comp}")
print(f"You choosed {you}")
a = game(comp, you)
if a==None:
    print("The game is a Tie")
elif a==True:
    print("You Win!")
elif a==False:
    print("You Lose!")