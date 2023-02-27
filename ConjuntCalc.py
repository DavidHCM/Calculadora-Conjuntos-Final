import random
from itertools import chain, combinations


def ConjAlet():
    global ConjUno
    global ConjDos
    
    ca1 = int(input("Cuantos conjuntos van a ser (max 2)? "))
    if ca1 == 1:
        ca2 = int(input("\nQue longitud tendra el primero conjunto (max 20)? "))
        while len(ConjUno)<ca2:
            ConjUno.add(random.randint(1,50))
    else:

        ca3 = int(input("\nQue longitud tendra el primero conjunto (max 20)? "))

        while len(ConjUno)<ca3:
            ConjUno.add(random.randint(1,50))
        
        ca4 = int(input("\nQue longitud tendra el segundo conjunto (max 20)? "))

        while len(ConjDos)<ca4:
            ConjDos.add(random.randint(1,50))


    print("Los conjuntos se han generado, son: ")
    global pot1len
    pot1len = len(ConjUno)
    print(sorted(ConjUno))
    print(sorted(ConjDos))

    ConjOpc()

#-------------------------------------------------------------------------------
def ConjInd():
    global ConjUno
    global ConjDos


    ka1 = int(input("Cuantos conjuntos van a ser (max 2)? "))

    if ka1 == 1:
        cont1 = int(input("Cual sera la longitu del conjunto A: "))

        for sent1 in range(cont1):
            k1=int(input("Ingresa el elemento numero {} del conjunto: ".format(sent1)))

            ConjUno.add(k1)


            sent1 += 1

    else:
        cont1 = int(input("Cual sera la longitu del conjunto A: "))

        for sent1 in range(cont1):
            k1=int(input("Ingresa el elemento numero {} del conjunto: ".format(sent1)))

            ConjUno.add(k1)


            sent1 += 1

        Cont2 = int(input("Cual sera la longitu del conjunto B: "))

        for sent2 in range(Cont2):
            k2=int(input("Ingresa el elemento numero {} del conjunto: ".format(sent2)))


            ConjDos.add(k2)

            sent2 += 1


    print("Los conjuntos se han generado, son: ")

    global pot1len
    pot1len = len(ConjUno)
    pot2len = len(ConjDos)

    print(sorted(ConjUno))
    print(sorted(ConjDos))

    ConjOpc()

#-------------------------------------------------------------------------------

def InterAB():
    InAB = set()
    for a in try1:
        if a in try2:
            InAB.add(a)
    
    print("Intersección A∩B: ",sorted(InAB))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

#-------------------------------------------------------------------------------
def UniAB():
    UnAB = set()
    UnAB = try1 | try2
    print("Unión A∪B: ",sorted(UnAB))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

#-------------------------------------------------------------------------------


def Dif1():
    Dif1to1 = set()
    for a in try1:
        if a not in try2:
            Dif1to1.add(a)

    print("Diferencia A-B: ",sorted(Dif1to1))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

#-------------------------------------------------------------------------------

def Dif2():
    Dif1to2 = set()
    for a in try2:
        if a not in try1:
            Dif1to2.add(a)

    print("Diferencia B-A: ",sorted(Dif1to2))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

#-------------------------------------------------------------------------------
def DifSim():
    DifSim1 = set()
    for a in try1:
        if a not in try2:
            DifSim1.add(a)
#Se tiene que evaluar la misma lista denuevo para hacer la diferencia con el segundo conj.
    for a in try2:
        if a not in try1:
            DifSim1.add(a)

    print("Diferencia simétrica: ",sorted(DifSim1))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ComplConjUno():
    
    CompleUno = set()
    for a in Unive:
        if a not in ConjUno:
            CompleUno.add(a)

    print("Complemento de A: ",sorted(CompleUno))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ComplConjDos():
    
    CompleDos = set()
    for a in Unive: # Solo revisamos un universo con un intervalo de 0 a 50.
        if a not in ConjDos:
            CompleDos.add(a)

    print("Complemento de B: ",sorted(CompleDos))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ProdCartUno():
    ProdCart1 = set()
    for a in try1:
        for b in try2:
           
            ProdCart1.add(("{},{}".format(a,b)) )
            
    
    print("Producto cartesiano AxB: ",sorted(ProdCart1))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ProdCartDos():
    ProdCart2 = set()
    for a in try2:
        for b in try1:
            ProdCart2.add(("{},{}".format(a,b)) )
            
    
    print("Producto cartesiano BxA: ",sorted(ProdCart2))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ProdCartTres():
    ProdCart3 = set()
    for a in try1:
        for b in try1:
           
            ProdCart3.add(("{},{}".format(a,b)) )
            
    
    print("Producto cartesiano AxA: ",sorted(ProdCart3))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def ProdCartCuat():
    ProdCart4 = set()
    for a in try2:
        for b in try2:
           
            ProdCart4.add(("{},{}".format(a,b)) )
            
    
    print("Producto cartesiano BxB: ",sorted(ProdCart4))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def Pot1():
    #Siendo sincero lo que es el conjunto potenia de el A y B, se obtuvieron por una libreria, esto ya que al tratar de...
    #Hacerlo la memoria no era suficiente al poder haber hasta: 1,048,576 combinaciones.

    

    def powt(ConjUno):
        
        return chain.from_iterable(combinations(list(ConjUno), a) for a in range(len(ConjUno)+1))

    print("Conjunto potencia A:", list(powt(ConjUno)))



    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

# Referencia: https://docs.python.org/3/library/itertools.html

#-------------------------------------------------------------------------------
def Pot2():
    #De igual manera aqui se uso de una libreria para poder hacer el conjunto potencia.
    def powt(ConjUno):
        return chain.from_iterable(combinations(list(ConjDos),a) for a in range(len(ConjUno)))

    print("Conjunto potencia A:", list(powt(ConjDos)))

    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

# Referencia: https://docs.python.org/3/library/itertools.html

#-------------------------------------------------------------------------------
def Card1():

    print("Cardinalidad de A: ",len(ConjUno))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def Card2():

    print("Cardinalidad de B: ",len(ConjDos))
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()

#-------------------------------------------------------------------------------
def Cont1():
    a4 = False
    for a in try1:
        if a in try2:
            a4 = True

    print("Contención A⊆B (Verdadero o falso): ",a4)
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------
def Cont2():
    a1 = False
    for a in try2:
        if a in try1:
            a1 = True

    print("Contención B⊆A (Verdadero o falso): ",a1)
    print("\n")
    print(("-----------------------------------------------------------------"))
    print("\n")
    ConjOpc()
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def ConjOpc():
    print("-----------------------------------------------------------------")
    opcConj = int(input("Estas son las siguientes opciones para usar los conjuntos: \n1. Intersección A∩B \n2. Unión A∪B \n3. Diferencia A-B \n4. Diferencia B-A \n5. Diferencia simétrica \n6. Complemento de A \n7. Complemento de B \n8. Producto cartesiano AxB \n9. Producto cartesiano BxA \n10. Producto cartesiano AxA \n11. Producto cartesiano BxB \n12. Conjunto potencia A \n13. Conjunto potencia B \n14. Cardinalidad de A \n15. Cardinalidad de B \n16. Contención A⊆B (Verdadero o falso) \n17. Contención B⊆A (Verdadero o falso) \n18. Salir del programa: "))
    if opcConj == 1:
        InterAB()
    
    elif opcConj == 2:
        UniAB()

    elif opcConj == 3:
        Dif1()

    elif opcConj == 4:
        Dif2()

    elif opcConj == 5:
        DifSim()
    
    elif opcConj == 6:
        ComplConjUno()

    elif opcConj == 7:
        ComplConjDos()

    elif opcConj == 8:
        ProdCartUno()

    elif opcConj == 9:
        ProdCartDos()

    elif opcConj == 10:
        ProdCartTres()

    elif opcConj == 11:
        ProdCartCuat()

    elif opcConj == 12:
        Pot1()

    elif opcConj == 13:
        Pot2()

    elif opcConj == 14:
        Card1()

    elif opcConj == 15:
        Card2()

    elif opcConj == 16:
        Cont1()

    elif opcConj == 17:
        Cont2()

    elif opcConj == 18:
        exit()


#Aqui un ciclo while para mantener el menu abierto en todo momento
ConjUno=set()
ConjDos=set()
Unive=set(range(0,50))
try1= ConjUno
try2= ConjDos

a2 = True
while a2 is True:
    
    mainMenu = int(input("1°Usar conjuntos generados aleatoriamente: \n2°Escribir los conjuntos: \n3°Salir: "))
    if mainMenu == 1:
        ConjAlet()

    elif mainMenu == 2:
        ConjInd()

    #Despedida
    elif mainMenu == 3:
        print("Gracias por usar el programa.")
        a2 = False

