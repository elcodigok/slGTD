#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import gettext

try:
	from snack import *
except ImportError:
	print gettext.gettext('newt library not installed')

class Datos:
	def __init__(self, archivo, titulo, texto, screen=None):
		self.archivo = archivo
		self.titulo = titulo
		self.texto = texto
		self.screen = screen

	def altas(self):
		layoutGrid = Grid(2, 4)
		boton = ButtonBar(self.screen, ((gettext.gettext("Accept"), "accept"), (gettext.gettext("Back"), "back")))
		recordTask = Entry(30, "")
		recordDate = Entry(15, str(date.today().isoformat()))
		layoutGrid.setField(Label(gettext.gettext("Task")), 0, 0, padding = (0, 0, 2, 0), anchorLeft=1)
		layoutGrid.setField(recordTask, 1, 0, anchorLeft = 1)
		layoutGrid.setField(Label(gettext.gettext("Date")), 0, 1, padding = (0, 1, 2, 0), anchorLeft=1)
		layoutGrid.setField(recordDate, 1, 1, anchorLeft = 1, padding = (0, 1, 2, 0))
		
		formAdd = GridFormHelp(self.screen, self.titulo, help, 1, 3)
		formAdd.add(layoutGrid, 0, 1, padding = (0, 0, 0, 1))
		formAdd.add(boton, 0, 2, growx=1)
		
		resultado = formAdd.runOnce()
		
		if (boton.buttonPressed(resultado) == "accept"):
			self.archivoEntrada = open(self.archivo, "a")
			self.archivoEntrada.write(recordTask.value())
			self.archivoEntrada.write("\t:created" + recordDate.value())
			self.archivoEntrada.write("\t:pNone"  + "\n")
			self.archivoEntrada.close()