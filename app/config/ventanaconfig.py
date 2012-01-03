#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser

try:
	import snack
except ImportError:
	raise ImportError("La libreria Newt no esta instalada.")


class VentanaConfiguracion:
	def __init__(self, archivo, titulo, texto, screen=None):
		self.archivo = archivo
		self.titulo = titulo
		self.texto = texto
		self.screen = screen

	def modificarConfiguracion(self):
		config = ConfigParser.RawConfigParser()
		config.read(self.archivo)
		banned_ip = config.get('Datos', 'banned_ip')
		banned_site = config.get('Datos', 'banned_site')
		banned_extension = config.get('Datos', 'banned_extension')
		exception_ip = config.get('Datos', 'exception_ip')
		exception_site = config.get('Datos', 'exception_site')
		exception_extension = config.get('Datos', 'exception_extension')
		archivo_log = config.get('Datos', 'logging')
		gw = config.get('Datos', 'default_gateway')
		(buttons, valores) = snack.EntryWindow(self.screen,
											self.titulo,
											self.texto,
											[('IP Bloqueadas', banned_ip),
												('IP Liberadas', exception_ip),
												('Dominios Bloqueados', banned_site),
												('Dominios Liberados', exception_site),
												('Extensiones Bloqueadas', banned_extension),
												('Extensiones Liberadas', exception_extension),
												('Archivo LOG', archivo_log),
												('Default Gateway', gw)],
											width=40,
											buttons=['Aceptar', 'Cancelar'])
		config = ConfigParser.RawConfigParser()
		config.add_section('Datos')
		config.set('Datos', 'banned_ip', valores[0])
		config.set('Datos', 'exception_ip', valores[1])
		config.set('Datos', 'banned_site', valores[2])
		config.set('Datos', 'exception_site', valores[3])
		config.set('Datos', 'banned_extension', valores[4])
		config.set('Datos', 'exception_extension', valores[5])
		config.set('Datos', 'logging', valores[6])
		config.set('Datos', 'default_gateway', valores[7])
		if (buttons == "aceptar"):
			configfile = open(self.archivo, "wb")
			config.write(configfile)
