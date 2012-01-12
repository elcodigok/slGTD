#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import gettext

try:
	import snack
except ImportError:
	raise ImportError("La libreria Newt no esta instalada.")


class Datos:
	def __init__(self, archivo, titulo, texto, screen=None):
		self.archivo = archivo
		self.titulo = titulo
		self.texto = texto
		self.screen = screen

	def altas(self):
		sg = snack.Grid(2, 4)
		boton = snack.ButtonBar(self.screen, ((gettext.gettext("Accept"), "accept"), (gettext.gettext("Back"), "back")))
		descripcion = snack.Entry(30, "")
		recordDate = snack.Entry(15, str(date.today().isoformat()))
		textoLabel = snack.Label(self.texto)
		sg.setField(snack.Label(gettext.gettext("Task")), 0, 0, padding = (0, 0, 2, 0), anchorLeft=1)
		sg.setField(descripcion, 1, 0, anchorLeft = 1)
		sg.setField(snack.Label(gettext.gettext("Date")), 0, 1, padding = (0, 1, 2, 0), anchorLeft=1)
		sg.setField(recordDate, 1, 1, anchorLeft = 1, padding = (0, 1, 2, 0))
		
		formAdd = snack.GridFormHelp(self.screen, self.titulo, help, 1, 3)
		formAdd.add(sg, 0, 1, padding = (0, 0, 0, 1))
		formAdd.add(boton, 0, 2, growx=1)
		
		resultado = formAdd.runOnce()
		
		if (boton.buttonPressed(resultado) == "accept"):
			self.archivoEntrada = open(self.archivo, "a")
			self.archivoEntrada.write(descripcion.value())
			self.archivoEntrada.write("\t:created" + recordDate.value())
			self.archivoEntrada.write("\t:pNone"  + "\n")
			self.archivoEntrada.close()

	def busqueda(self):
		(boton, descripcion) = snack.EntryWindow(self.screen,
												self.titulo,
												self.texto,
												['Buscar'],
												width=40,
												entryWidth=30,
												buttons=['Aceptar', 'Cancelar'])