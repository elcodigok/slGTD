#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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
			self.titulo = "Sin Titulo"

	def leerArchivo(self):
		if os.path.exists(self.archivo):
			self.archivoEntrada = open(self.archivo, "r")
			self.lineaArchivo = self.archivoEntrada.readlines()
			self.archivoEntrada.close()
		else:
			self.lineaArchivo = "Sin registros"
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
		while (opcion != "volver"):
			self.contenido = self.leerArchivo()
			self.label = snack.Label(self.texto)
			self.botones = snack.ButtonBar(self.screen,
										(("Agregar", "agregar"),
										("Borrar", "borrar"),
										("Volver", "volver")))
			self.lista = snack.Listbox(height=13,
									width=45,
									returnExit=1,
									showCursor=0,
									scroll=1)
			for registro in self.contenido:
				self.lista.append(registro, registro)
			self.grid = snack.GridForm(self.screen, self.titulo, 1, 3)
			self.grid.add(self.label, 0, 0, growx=0, growy=0, anchorLeft=1)
			self.grid.add(self.lista, 0, 1)
			self.grid.add(self.botones, 0, 2, growx=1, growy=0)
			respuesta = self.grid.runOnce()
			opcion = self.botones.buttonPressed(respuesta)
			if (opcion == "agregar"):
				cargaDeValores = Datos.Datos(self.archivo,
											"Nuevo",
											self.texto,
											self.screen)
				cargaDeValores.altas()
			elif (opcion == "borrar"):
				self.guardarArchivo(self.lista.current())
