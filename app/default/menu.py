#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	import snack
except ImportError:
	raise ImportError("La libreria Newt no esta instalada.")


class Menu:
	def __init__(self, titulo, texto, opciones, screen=None):
		self.titulo = titulo
		self.texto = texto
		self.screen = screen
		if (titulo == ""):
			self.titulo = 'Sin Titulo'
		self.items = []
		for item in opciones:
			self.items.append(item)

	def mostrarMenu(self):
		(self.button, rta) = snack.ListboxChoiceWindow(self.screen,
													self.titulo,
													self.texto,
													self.items,
													width=45,
													height=10,
													scroll=0,
													buttons=("Aceptar", "Cancelar"))
		if (self.button == 'Cancelar'):
			self.screen.finish()
			rta = None
		return rta