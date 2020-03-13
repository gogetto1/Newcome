import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
    
def koniec_programu():
    print("Dziekuje za skorzystanie. Do zobaczenia wkrótce")
    return 

print("Witam w programie liczącym powierzchnię figur.Wybierz jaką figurę chcesz policzyć:\n\
1 - prostokąt\n\
2 - kwadrat\n\
3 - trójkąt\n\
4 - trapez\n\
5 - koło\n\
6 - zamknięcie kalkulatora")
      
     
while True:
    
    wybor = input("Wybierz cyfrę do odpowiedniej figury lub zakończenia programu: ")

    if wybor == "1":
        a = int(input("Podaj pierwszy bok prostokąta: "))
        b = int(input("Podaj drugi bok prostokąta: "))
        print("Pole prostokąta wynosi",pole_prostokata(a, b))

    elif wybor == "2":
        a = int(input("Podaj bok kwadratu: "))
        print("Pole kwadratu wynosi",pole_kwadratu(a))
        
    elif wybor == "3":
        a = int(input("Podaj podstawe trójkąta: "))
        h = int(input("Podaj wysokość trójkąta "))
        print("Pole trójkąta wynosi",pole_trojkata(a, h))

    elif wybor == "4":
        a = int(input("Podaj pierwszą podstawe trapezu: "))
        b = int(input("Podaj drugą podstawe trapezu: "))
        h = int(input("Podaj wysokość trapezu "))
        print("Pole trapezu wynosi",pole_trapezu(a, b, h))
        
    elif wybor == "5":
        r = int(input("Podaj pierwszą promień koła: "))
        print("Pole koła wynosi",pole_kola(r))


    elif wybor == "6":
        koniec_programu()
        break

    else:
        print("Zły znak. Spróbuj ponownie! Wybierz jaką figurę chcesz policzyć:\n\
1 - prostokąt\n\
2 - kwadrat\n\
3 - trójkąt\n\
4 - trapez\n\
5 - koło\n\
6 - zamknięcie kalkulatora")
        

