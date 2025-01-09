import csv

#todo Aufgabe 0
#ERstelle Variable

n_loop = 0



#todo Aufgabe 1
#gib alle Zahlen von 1 bis 100 aus

i = 1
while i <= 100:
    print(i)
    i = i + 1

#todo Aufgabe 2
#ersetze alle Zahlen, die durch drei Teilbar sind mit String "digital"

i = 1
while i <= 100:
    if i % 3 == 0:
        print("Digital")
    else:
        print(i)
    i = i + 1


m = 1
while m <= 100:
    if m % 5 == 0:
        print("Digital")
    else:
        print(m)
    m = m + 1


#Aufgabe 4
#ersetze alle Zahlen, die durch drei Teilbar sind mit String "digital" und durch 5 mit "history"
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0: #oder einmal durch 15
        print("digital history")
    elif i % 3 == 0:
        print("Digital")
    elif i % 5 == 0:
        print("History")
    else:
        print(i)
    i = i + 1



#Aufgabe 5
with open("persons.txt", encoding="utf-8", newline="", mode="r") as f:
    #print(f.readlines()[4])
    print(f.readlines()[4][4])






