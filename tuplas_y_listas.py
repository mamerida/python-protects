t = (89766, "Alicia", "Hacker", (9, "Julio", 1988))
a = len(t)
#print(t[3])
#print(a)

#empaquetar tuplas
""" Si a una variable se le asigna una secuencia de valores separados por comas, 
el valor de esavariable será la tupla formada por todos los valores asignados"""

q = 1
w = "a"
e = 2
r = q,w,e  # los separo con , 
print(r)
"""
Si se tiene una tupla de longitud k,
 se puede asignar la tupla a k variables distintas y 
 en cada variable quedará una de las componentes de la tupla.
 A esta operación se la denomina
 desempaquetado de tuplas
 """
x,y,z = r

print(x)
print(y)
print(z)

"""cartas como tuplas"""
"""
a)  Proponer una representación con tuplas para las cartas de la baraja francesa.
b)  Escribir una función poker que reciba cinco cartas de la baraja francesa 
e informe (de-vuelva el valor lógico correspondiente) si esas cartas forman o no un poker
(es decir quehay 4 cartas con el mismo número)
"""
carta1=("A","picas")
carta2=(1,"corazones")
carta3=(2,"trebol")
carta4=(3,"Diamante")

def poker(c1,c2,c3,c4):
	if c1[0] == c2[0] == c3[0] == c4[0]:
		print("Felicidades, tienes un poker")
		return True
	else:	
		print("Que lastimas, no tienes poker")
		return False

c1=(1,"picas")
c2=(1,"picas")
c3=("A","trebol")
c4=(1,"corazones")

"""
 Escribir una función sumaTiempoque reciba dos tiempos dados y devuelva su suma.
"""

def sumaTiempo(t1,t2):
	suma =()
	hora = 0
	mint = t1[0]+t2[0]
	if mint > 60:
		mint = mint - 60
		hora = hora + 1 
	seg = t1[1]+t2[1]
	if seg > 60:
		seg = seg-60
		mint = mint +1 
	suma = hora,mint,seg
	print("hola")
	return print(suma)


t1=(30,40)
t2=(40,60)

"""
Escribir una función diaSiguienteE que dada una fecha expresada
calcule el día siguiente al dado, en el mismo formato (Dia,Mes,Año) numero entero
"""
def diaSiguienteE(fecha):
	fechaSig = ()
	if fecha[1] == 2:
		if fecha[0] ==28:
			a = 1
			b = 3
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
		else:
			a = fecha[0]+1
			b = 2
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
	elif fecha[1] == 1 or fecha[1] == 3 or fecha[1] == 5 or fecha[1] == 7 or fecha[1] == 8 or fecha[1] == 10:
		if fecha[0] == 31:
			a = 1
			b = fecha[1]+1
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
		else: 
			a = fecha[0]+1
			b= fecha[1]
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
	elif fecha[1]==12:
		if fecha[0] == 31:
			a = 1 
			b = 1
			c = fecha[2] + 1 
			fechaSig = a,b,c
			return print(fechaSig)
		else:
			a = fecha[0]+1
			b = fecha[1]
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
	else:
		if fecha[0] == 30:
			a = 1
			b = fecha[1] + 1
			c = fecha[2]
			fechaSig = a,b,c
			return print(fechaSig)
		else:
			a= fecha[0]+1
			b = fecha[1]
			c = fecha[2]
			fechaSig =a,b,c
			return print(fechaSig)

"""
perdir legajos hasta terminar
"""

def listaLeg():
	lista=[]
	print("Por favor ingrese los legajos que desea cargar")
	print("Cuando haya terminado por favor coloque un 0 para finalizar")
	#Tomamos el input de la perosna 
	leg =int(input("Por favor introduzca el legajo "))
	#llenamos la lista
	while leg > 0:
		leg =int(input("Por favor introduzca el legajo "))
		lista.append(leg)


	#imprimimos el resultado
	print("A creado la siguiente lista de legajos ")
	print(lista)
	return lista

"""
perdir legajos hasta terminar no se puede repetir legajo 
"""
def listaLeg2():
	lista=[]
	print("Por favor ingrese los legajos que desea cargar")
	print("Cuando haya terminado por favor coloque un 0 para finalizar")
	print("No se pueden colocar legajos repetidos")
	#Tomamos el input de la perosna 
	leg =int(input("Por favor introduzca el legajo "))	
	while leg > 0:
		if leg in lista :
			print("El numero que desea ingresar ya existe")
			leg =int(input("Por favor introduzca el legajo "))

		else:
			
			lista.append(leg)
			leg =int(input("Por favor introduzca el legajo "))

	#imprimimos el resultado
	print("A creado la siguiente lista de legajos ")
	print(lista)
	return lista


"""
Ejercicio 7.9.Escribir una función que reciba como parámetro una cadena de palabras
 separadas por espacios y devuelva
 , como resultado, cuántas palabras de más de cinco letras tiene lacadena dada
"""

def sep(cadena):
	a = 0 
	cad = cadena.split()
	print(cad)
	for i in cad:
		if len(i) > 5:
			a = a + 1
		else:
			pass

	print("el numero de palabras es : ", a)	
"""
Ejercicio 7.10 Telegrama
"""

def telegram(cadena,maxi,precorto,preclarga):
	cad = cadena.split()
	tel = []
	costo = 0 
	#determinar el precio del telegrama
	for i in cad:
		if len(i) > maxi:
			costo = costo + preclarga
		else:
			costo = costo + precorto

	#realizar el telegrama cortado
	for i in cad:
		if len(i) < maxi and i != ".":
			tel.append(i)
		elif i == ".":
			tel.append("STOP")
		else:
			i = i[0:maxi-1] +"@"
			tel.append(i)
	tel.append("STOPSTOP")

	return print("El telegrama es el siguiente \n",tel,"\n cuyo costo es ",costo)

telegram("hola . apresurado",5,1,2)

