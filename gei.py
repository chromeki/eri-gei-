def op1():
    print("1) No")

def op2():
    print("1) Sí")

print("hola")
saludo = str(input("Respuesta: "))

x = True

while(x):
    y= True

    while(y):
        print("¿eres gei?")
        print("1) Sí")
        print("2) No")

        try:
            rp1 = int(input("Respuesta: "))
            y = False
        except:
            print("ponga un valor válido tonoto")

    if(rp1 == 1):
        x = False
        f = 1
    elif(rp1 == 2):
        x = False
        f = 2
    else:
        print("Inserte un valor de las respuestas bobo")

x = True

while(x):
    y = True
    while(y):
        print("¿estás mintiendo?")

        if(f==1):
            op1()
        else:
            op2()

        try:
            rp2 = int(input("Respuesta: "))
            y = False
        except:
            print("Inserte un valor válido troilo")
    
    if(rp2 == 1):
        x = False
    else:
        print("Inserte una opción gei")
    



print("jaja alto gei")
