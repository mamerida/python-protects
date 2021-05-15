
def es_numero(valor):
	return isinstance(valor,(int,float,complex))
class Punto(object):
	def distancia(self,otro):
		dx = self.x - otro.x
		dy = self.y - otro.y
		return (dx*dx +dy*dy)**0.5
		#crea un nuevo punto con la resta de los dos actuales 
	def restar(self,otro):
		return Punto(self.x-otro.x,self.y - otro.x)
		#crea la normal del punto
	def norma(self):
		return(self.x*self.x + self.y*self.y)**0.5
	def distancia(self, otro):
		""" Devuelve la distancia entre ambos puntos. """
		r = self.restar(otro)
		return r.norma()
	""" para yo poder sumar o restar elementos de mi objeto tengo qeu crear la funcion si no, no va a hacer nada"""
	def __add__ (self,otro):
		return Punto(self.x + otro.x , self.y + otro.y)
	def __sub__ (self,otro):
		return Punto(self.x - otro.x , self.y - otro.y)
	"""docstring for Punto"""
	def __init__(self, x =0 , y = 0):
		""" Constructor de Punto, x e y deben ser numéricos,de no ser así, se levanta una excepción TypeError """
		if es_numero(x) and es_numero(y):
			self.x = x 
			self.y = y
		else:
			raise TypeError ("x e y deben ser valores numéricos")

	def __str__(self):
		return "("  + str(self.x) + ", " + str(self.y) + ")"


p = Punto(3,4)
q = Punto(2,5)

print(p +q)
print("----------")
print(p-q)