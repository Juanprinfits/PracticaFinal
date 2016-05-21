#!/usr/bin/env python
# -*- coding: utf-8 -*-
#	Juan Príncipe Ovelleiro
#	Juan José García Fonsecaç
#
#  juagarc.py

import pygtk
pygtk.require("2.0")
import gtk

class juego:				
				
				
	def __init__(self):
		filas = 10
		columnas = 10
		self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)                  #crea ventana y la pone por encima
		self.ventana.set_border_width(100)								#pone el tamaño de la ventana
		tablero=gtk.Table(filas,columnas, homogeneous=True)
		botones = []
		for i in range(len(botones)):#imprime letras en orden          
			for j in range(len(botones[0])):
				botones[i] = [gtk.Button[str(i)] * columnas+4
				y = filas%i
				table.attach(botones[i], i,i+1, y,y+1)
				botones[i].show()
		self.ventana.add(tablero)
		self.ventana.show_all()
		
	def main(self):
		gtk.main()
		



if __name__ == '__main__':
	prueba = juego()
	prueba.main()
