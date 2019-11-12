from piezas.pieza import *

# HERENCIA PIEZA
"""REY"""
class Rey(Pieza):

	corona = False
	descriptor = ""

	def __init__(self, team, enemy, posicionX, posicionY):

		Pieza.__init__(self, team, enemy, self.corona)
		self.posicionX = posicionX
		self.posicionY = posicionY
		self.descriptorBlanco = "Rv"
		self.descriptorNegro = "R^"
		self.tipo = 'REY'
		if(self.team == 'blanco'):
			self.descriptor = self.descriptorBlanco
		elif(self.team == 'negro'):
			self.descriptor = self.descriptorNegro

	def __str__(self):
		return self.descriptor

	@staticmethod
	def movimiento(x, y, pieza, equipo, colorPiezaEnemiga, piezaMovida):

		movimientoValido = False

		if(x == 1 and y == 1 ):
			print('Movimiento en diagonal hacia adelante derecha')
			movimientoValido = True
		elif( x == -1 and y == 1):
			print('Movimiento en diagonal hacia adelante izquiera')
			movimientoValido = True
		if(x == -1 and y == -1 ):
			print('Movimiento en diagonal hacia abajo izquiera')
			movimientoValido = True
		elif( x == 1 and y == -1):
			print('Movimiento en diagonal hacia abajo derecha')
			movimientoValido = True
		elif(x == 1 and y == 0):
			print('Movimiento hacia la izquierda')
			movimientoValido = True
		elif(x == -1 and y == 0):
			print('Movimiento hacia la derecha')
			movimientoValido = True
		elif(y == -1 and x == 0):
			print('Movimiento en retroceso')
			movimientoValido = True
		elif(y == 1 and x == 0):
			print('Movimiento hacia adelante')
			movimientoValido = True

		# Validamos que el movimiento sea válido
		if(self.validaMovimiento(movimientoValido, pieza, colorPiezaEnemiga)):
			self.posicionX = self.posicionX + x
			self.posicionY = self.posicionY + int(self.multiplicadorY)*y
			return '{}, {}'.format(self.posicionX, self.posicionY)
		else:
			return 'Movimiento inválido'
		pass
