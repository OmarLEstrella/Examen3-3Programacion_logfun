"""
    Lopez Lira Alexis
    Lopez Estrella Omar


 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:

	def gprimo(N):
		pass


	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
    print(" ")
"""
print("Ejercicio Generadores Primos")
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

"""

¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud


"""

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
