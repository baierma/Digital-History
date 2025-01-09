


while True:
    n = int(input("Wie viel Kaffee hast du Getrunken?"))
    if n <= 8:
        print("Die Kaffeeanzahl ist vertretbar")
        break
    else:
        print("Du bist zu hibbelig, bist du dir sicher, dass du so viel getrunken hast?")




quit()

import random

names =["Jasmin", "Theodor", "Mil", "Maxi", "Markus", "Kilian", "Sophie", "Mika", "Bastolomaeus"]

def name_generator():
    while True:
        x = str(input("Wollen Sie einen zufälligen Namen? "))

        if x == "yes":
            print(random.choice(names))
            break
        elif x == "no":
            print("Pech gehabt.")
            break
        else:
            print("Ich habe Sie nicht verstanden. Antworten Sie bitte mit 'yes' oder 'no'.")



name_generator()