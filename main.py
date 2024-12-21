import random
import sys

question = "Devinez le nombre ? :"

guess_number = random.randrange(1,100)

print("----Le jeu----")

i = 5
while i >= 1 :
    print(f"Il te reste {i} essai")
    answer = int(input(question))
    
    if guess_number > answer : 
        print("Nombre à deviné est plus grand")
        i -= 1
    elif guess_number < answer :
        print("Nombre à devini est plus petit")
        i -= 1
    elif guess_number == answer :
        print("Bravo tu as gagné")
        sys.exit()
print("Tu n'as pas réussi")
sys.exit()