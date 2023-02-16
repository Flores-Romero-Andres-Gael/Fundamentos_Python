def nuevoTema(tema):
    print("\n--------", tema , "--------\n") 

#Comentario en una linea 
nuevoTema("Operadores aritmeticos")
print("Operador divison entera: \nEjemplo: (10 // 3) =  ", 10 // 3) #Operador //
print("\nOperador potencia: \nEjemplo: (5 ** 3) = ", 5 ** 3) #Operador **

#Actividad: Imprimir la tabla de verdad de los operadores logicos.

nuevoTema("Operadores logicos")

print("\n---------------And--------------")
print("Ejemplo: (True and False): ", True and False)
print("Ejemplo: (True and True): ", True and True)
print("Ejemplo: (False and True): ", False and True)
print("Ejemplo: (False and False): ", False and False)

print("\n---------------Not--------------")
print("Ejemplo: (not True): ", not True)
print("Ejemplo: (not False): ", not False)

print("\n---------------Or---------------")
print("Ejemplo: (True Or True): ", True or True)
print("Ejemplo: (True Or False): ", True or False)
print("Ejemplo: (False Or True): ", False or True)
print("Ejemplo: (False Or False): ", False or False)

nuevoTema("Operadores de comparacion")
print("Ejemplos: ")
print("2 == 3: ", 2 == 3)
print("5 != 6: ", 5 != 6)
print("60 < 71: ", 60 < 71)
print("90 > 100: ", 90 > 100)
print("10000 <= 10000: ", 10000 <= 10000)
print("12 >= 11: ", 12 >= 11)

nuevoTema("Variables")
variable = 10
_variable2 = 6.2456
Variable3 = "Gael"
dosPalabras = "Hello"
dos_palabras = "Hello"

print(variable, _variable2, Variable3, dosPalabras, dos_palabras)

a, b, c = 10, 5.16, "Welcome"
print(a,b,c)

nuevoTema("Enteros")
w = 105
x = 999999999999999
y = -121
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x = 1297.50
y = 0.50594

print(x, type(x))
print(y, type(y))

nuevoTema("Numeros Complejos")
x = -46j 
y = 12+45j
z = 2j

print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = [8]
print(lis, "es" , bool(lis))
t = ()
print(t, "es" , bool(t))
new = "Hello"
print(new, "es" ,bool(new))
num = 99
print(num, "es" ,bool(num))
comp = 1 + 0j
print(comp, "es" ,bool(comp))
val = None #None equivale a NULL
print(val, "es" ,bool(val))

nuevoTema("Listas") #No son arreglos
a = [10, 20.5, "Python List"]
print(a)
print("a[1] =", a[1])
a[0] = "Hola"
print(a)

nuevoTema("Tuplas")
t = (25, "Tupla", 1+10j, 3.1416)
print(t)
print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])
#t[1]=34 No se pueden transcribir una tupla, Operacion no valida

nuevoTema("Sets")
t = {50,20,30,40,10,50}
print("Conjunto t = ", t, type(t))

nuevoTema("Diccionario")
d = {1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]: ", d["Valor2"])

nuevoTema("Cadenas")
Cadena1 = "Cadena con comillas dobles"
Cadena2 = 'Cadena con comillas simples'
Cadena3 = '''Cadena de varias lineas
con tabuladores
y saltos'''

print(Cadena1, type(Cadena1))
print(Cadena2, type(Cadena2))
print(Cadena3, type(Cadena3))

print(Cadena3)
print("Segmentacion de cadenas")
print(Cadena1[5:11])
print(Cadena1[:5])
print(Cadena1[7:])
print(Cadena1[-8:-1])
print(Cadena1[0:18:1])
print(Cadena1[0:18:2])
print(Cadena1[0:18:3])

Cadena1 = "Hola"
Cadena4 = (Cadena1 + " ")*5
print(Cadena4)

Cadena5 = Cadena4.capitalize()
print(Cadena5)
Cadena5 = Cadena4.upper()
print(Cadena5)

nuevoTema("Objetos Mutables")


nuevoTema("Objetos Inmutables")

