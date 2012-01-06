#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date

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
		(boton, (nombre, descripcion)) = snack.EntryWindow(self.screen,
														self.titulo,
														self.texto,
														['Nombre', 'Fecha'],
														width=40,
														entryWidth=30,
														buttons=['Aceptar', 'Cancelar'])
		
		if (descripcion != ""):
			self.archivoEntrada = open(self.archivo, "a")
			self.archivoEntrada.write(nombre)
			self.archivoEntrada.write("\t:created" + date.today().isoformat())
			self.archivoEntrada.write("\t:pNone"  + "\n")
		else:
			self.archivoEntrada = open(self.archivo, "a")
			self.archivoEntrada.write(nombre + "\n")
		self.archivoEntrada.close()

	def busqueda(self):
		(boton, descripcion) = snack.EntryWindow(self.screen,
												self.titulo,
												self.texto,
												['Buscar'],
												width=40,
												entryWidth=30,
												buttons=['Aceptar', 'Cancelar'])