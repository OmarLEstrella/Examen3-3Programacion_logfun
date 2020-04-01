"""
    Lopez Lira Alexis   16590484
    Lopez Estrella Omar 16590486


 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:

	def gprimo(N):
		pass

	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
"""
print("Ejercicio Generadores Primos")
def gprimo(N):
    def esPrimo(n):
        if n <= 1:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    n = 0
    while(n <= N):
        if esPrimo(n):
            yield n
        n = n + 1

a = gprimo(10)
z = [e for e in a]
print(z)
"""
Bada Boom!!! <generadores> 20 pts

	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"

	def genBadaBoom(N):
		pass

	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
print(" ")
print("Ejercicio Bada Boom!!")
def genBadaBoom(N):
    i = 0
    while i < N:
        i = i + 1
        Bada = i % 3 == 0
        Boom = i % 5 == 0
        if Bada and Boom:
            yield "Bada Boom!!"
        elif Bada:
            yield "Bada"
        elif Boom:
            yield "Boom!!"
        else:
            yield i

a = genBadaBoom(10)
z = [e for e in a]
print(z)
"""
Combinaciones <Comprensión de listas> 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)

	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
"""
print("")
print("Ejercicio Combinaciones")
camisas = ["Camisa roja","Camisa negra","Camisa azul","Camisa morada","Camisa cafe"]
pantalones = ["Pantalon negro","Pantalon azul","Pantalon cafe obscuro","Pantalon crema"]
accesorios = ["cinturon","tirantes","lentes","fedora"]

COMBINACIONES = [ [a,b,c] for a in camisas for b in pantalones for c in accesorios]
print(COMBINACIONES)
print("Cantidad de Combinaciones Posibles",len(COMBINACIONES))
"""

¿Fedora?  <Comprensión de listas >  15 pts
	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
"""
print("")
print("Ejercicio ¿Fedora?")
camisas = ["Camisa roja","Camisa negra","Camisa azul","Camisa morada","Camisa cafe"]
pantalones = ["Pantalon negro","Pantalon azul","Pantalon cafe obscuro","Pantalon crema"]
accesorios = ["cinturon","tirantes","lentes","fedora"]
COMBINACIONES = [ [a,b,c] for a in camisas for b in pantalones for c in accesorios]
COMBINACIONES_FEDORA = [i for i in COMBINACIONES if i[2] == "fedora"]
print(COMBINACIONES_FEDORA)
print("Combinaciones Disponibles",len(COMBINACIONES_FEDORA))
"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista.

"""
print(" ")
print(" Ejercicio Monads Lacrimosa")

from functools import reduce
print('\n')
#Este metodo me hace el conteo de la cantidad de letras que aparecen
# en el texto
def contar_veces2(elemento, lista):
    #contador
    veces = 0
    #Empieza a recorrer la lista acorde el elemento que le mando
    for i in lista:
        if elemento == i:
            veces += 1
    #Le sumo uno porque por lo menos aparece una vez en todo el texto esa letra
    return veces + 1

def unicos2(l, letras = False):
    if not letras:
        letras = []
    c = []
    n = []
    if not l:
        return []
    contar = []
    primero = l[0]
    #Extraigo cada caracter del texto
    for i in primero:

        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)
    if len(l) == 1:
        return letras
    else:
        #cuento cuantas veces aparce cada letra NO REPETIDA en el texto
        for a in c:
            #usando la funcion contar_veces, aqui le mando
            #la letra a evaluar y la lista
            contar.append(contar_veces2(a, n))
        #Cuenta el numero total de letras usando reduce
        v = reduce(lambda a,b: a + b, contar)
        #creo una lista de tuplas para relacionar cada elemento con su valor
        #de acuerdo a su indice entre las listas c y contar, ya
        #que son del mismo tamaño
        letras += [list(zip(c, contar))]
        print('Lista de letras que existen y su cantidad\n',letras)
        #La probabilidad es 1/Num.letras  porque por lo menos, esa letra
        #aparece una vez en todo el texto

        print('Probabilidad: 1 /',v,'En la cadena -->',primero,'\n')
        return unicos2(l[1:], letras)

letra = ['Die Suche endet jetzt und hier',
         'Gestein kalt und nass',
         'Granit in Deiner Brust',
         'Der Stein der Dich zerdrückt',
         'Der Fels der Dich umgibt',
         'Aus dem gehauen Du doch bist',
         'Despiertate te busco',
         'Mi corazon abreté te libro',
         'Elevate mi luz y prende mi llama',
         'Si a ti, yo se, te encontrare'
         ]
v = unicos2(letra)
#Esta es la lista con las otras listas dentro. Dentro de cada lista
#hay tuplas con la letra y el numero de veces que se repite.
print('Lista de letras que existen y su cantidad\n',v)
print(" ")
print("\nLetras con menos apariciones en el texto\n")
f1 = filter(lambda a: a[1] == 1,v[0])
f2 = filter(lambda a: a[1] == 1,v[1])
f3 = filter(lambda a: a[1] == 1,v[2])
f4 = filter(lambda a: a[1] == 1,v[3])
f5 = filter(lambda a: a[1] == 1,v[4])
f6 = filter(lambda a: a[1] == 1,v[5])
f7 = filter(lambda a: a[1] == 1,v[6])
f8 = filter(lambda a: a[1] == 1,v[7])
f9 = filter(lambda a: a[1] == 1,v[8])
d1 = list(f1)
d2 = list(f2)
d3 = list(f3)
d4 = list(f4)
d5 = list(f5)
d6 = list(f6)
d7 = list(f7)
d8 = list(f8)
d9 = list(f9)
print("En la linea 1",d1)
print("En la linea 2",d2)
print("En la linea 3",d3)
print("En la linea 4",d4)
print("En la linea 5",d5)
print("En la linea 6",d6)
print("En la linea 7",d7)
print("En la linea 8",d8)
print("En la linea 9",d9)
"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista.

"""
print(" ")
print("Ejercicio Monads Hole in my soul apocalyptica")
print('\n')
#Este metodo me hace el conteo de la cantidad de letras que aparecen
# en el texto
def contar_veces(elemento, lista):
    #contador
    veces = 0
    #Empieza a recorrer la lista acorde el elemento que le mando
    for i in lista:
        if elemento == i:
            veces += 1
    #Le sumo uno porque por lo menos aparece una vez en todo el texto esa letra
    return veces + 1

def unicos(l):
    contar = []
    c = []
    n = []
    if not l:
        return []
    primero = l[0]
    #Extraigo cada caracter del texto
    for i in primero:
        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)

    #cuento cuantas veces aparce cada letra NO REPETIDA en el texto
    for a in c:
        #usando la funcion contar_veces, aqui le mando
        #la letra a evaluar y la lista
        contar.append(contar_veces(a, n))
    #Cuenta el numero total de letras usando reduce
    v = reduce(lambda a,b: a + b, contar)
    #La probabilidad es 1/Num.letras  porque por lo menos, esa letra
    #aparece una vez en todo el texto
    print('Probabilidad: 1 /',v)
    #creo una lista de tuplas para relacionar cada elemento con su valor
    #de acuerdo a su indiceentre las listas c y contar ya
    #que son del mismo tamaño
    letras = list(zip(c, contar))
    print('Lista de letras que existen y su cantidad\n',letras)

    return letras

lis = ["""There's a hole in my heart, in my life, in my
     way And it's filled with regret and all I did, to push you away
    If there's still a place in your life, in your heart for me
    I would do anything, so don't ask me to leave
    I've got a hole in my soul where you use to be
    You're the thorn in my heart and you're killing me
    I wish I could go back and do it all differently
    I wish that I'd treated you differently
    'Cause now there's a hole in my soul where you use to be"""]

s = unicos(lis)
f = filter(lambda a: a[1] == 1, s)
d = list(f)
print('\nLetras con menos apariciones en el texto\n',d)
