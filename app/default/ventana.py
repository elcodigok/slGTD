#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import gettext
import datos as Datos

try:
	import snack
except ImportError:
	raise ImportError("La libreria Newt no esta instalada.")


class Ventana:
	def __init__(self, archivo, titulo, texto, screen=None):
		self.archivo = archivo
		self.titulo = titulo
		self.texto = texto
		self.screen = screen
		if (titulo == ""):
			self.titulo = gettext.gettext("No Title")

	def leerArchivo(self):
		if os.path.exists(self.archivo):
			self.archivoEntrada = open(self.archivo, "r")
			self.lineaArchivo = self.archivoEntrada.readlines()
			self.archivoEntrada.close()
		else:
			self.lineaArchivo = gettext.gettext("No Record")
		return self.lineaArchivo

	def posicionLista(self):
		posicion = self.lista.current()
		return posicion

	def guardarArchivo(self, elemento):
		if os.path.exists(self.archivo):
			self.archivoEntrada = open(self.archivo, "w")
			for linea in self.contenido:
				if (linea != elemento):
					self.archivoEntrada.write(linea)
			self.archivoEntrada.close()

	def mostrarListado(self):
		opcion = ""
		while (opcion != "back"):
			self.contenido = self.leerArchivo()
			self.label = snack.Label(self.texto)
			self.botones = snack.ButtonBar(self.screen,
										((gettext.gettext("Add"), "add"),
										(gettext.gettext("Delete"), "delete"),
										(gettext.gettext("Back"), "back")))
			self.lista = snack.Listbox(height=13,
									width=60,
									returnExit=1,
									showCursor=0,
									scroll=1)
			for registro in self.contenido:
				fecha = registro.split("\t")[1]
				recordView = registro.split("\t")[0] + "(" + fecha.strip(":created") + ")"
				self.lista.append(recordView, registro)
			self.grid = snack.GridForm(self.screen, self.titulo, 1, 3)
			self.grid.add(self.label, 0, 0, growx=0, growy=0, anchorLeft=1)
			self.grid.add(self.lista, 0, 1)
			self.grid.add(self.botones, 0, 2, growx=1, growy=0)
			respuesta = self.grid.runOnce()
			opcion = self.botones.buttonPressed(respuesta)
			if (opcion == "add"):
				cargaDeValores = Datos.Datos(self.archivo,
											gettext.gettext("New"),
											self.texto,
											self.screen)
				cargaDeValores.altas()
			elif (opcion == "delete"):
				self.guardarArchivo(self.lista.current())
