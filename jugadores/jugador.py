
class Jugador():

	def __init__(self, equipo, equipoContrario):

		self.equipo = equipo
		self.equipoContrario = equipoContrario
		self.movimiento = 0
		self.tiempo = 0
		self.PIEZAS_CAPTURADAS = []

		pass

	# Método para introducir pieza capturada en el tablero
	@staticmethod
	def introducirPieza(jugador, tablero, indexPieza):
		# Evaluamos que la ubicación en el tablero este desocupada
		xy = input("Ingrese el lugar donde quiere ingresar la pieza (fila, columna separadas por espacio)\n")
		if((tablero[int(xy[0])][int(xy[2])] == "   " or tablero[int(xy[0])][int(xy[2])] == "  ") and int(len(jugador.__dict__['PIEZAS_CAPTURADAS'])) != 0):
			# Obtenemos la pieza de la lista de piezas capturadas
			newPieza = jugador.__dict__['PIEZAS_CAPTURADAS'][indexPieza]
			jugador.__dict__['PIEZAS_CAPTURADAS'].pop(indexPieza)
			# Cambiamos el equipo de la pieza capturada (al reproducir nuevamente el tablero aparecerá con el símbolo que corresponde)
			newPieza.cambiarEquipo(jugador.__dict__['equipo'])
			# Si la pieza se corona, le ponemos en falso este campo
			if(newPieza.__dict__['corona'] == True):
				newPieza.__dict__['coronado'] = False
			# Retornamos el tablero. Deberemos inicializarlo nuevamente.
			tablero[int(xy[0])][int(xy[2])] = newPieza

			return tablero
		else:
			return False
