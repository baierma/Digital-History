
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
