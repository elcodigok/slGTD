#!/usr/bin/env python
# -*- coding: utf-8 -*-
#''' Sistema de control de Tareas '''
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

import commands
import ConfigParser
import logging
import os
import sys

import lib.ping as ping
import lib.IPy as IP
import app.default.menu as Menu
import app.default.ventana as Ventana
import app.config.ventanaconfig as Configuracion

try:
	import snack
except ImportError:
	raise ImportError("La libreria Newt no esta instalada.")

config = ConfigParser.RawConfigParser()
config.read(os.getcwd() + "/config/gtd.cnf")

path_logging = config.get('Datos', 'logging')
logging.basicConfig(level=logging.INFO,
					format='%(asctime)s %(levelname)-8s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename=path_logging)
logger = logging.getLogger(path_logging)

path_banned_ip = config.get('Datos', 'banned_ip')
path_banned_site = config.get('Datos', 'banned_site')
path_banned_extension = config.get('Datos', 'banned_extension')

path_exception_ip = config.get('Datos', 'exception_ip')
path_exception_site = config.get('Datos', 'exception_site')
path_exception_extension = config.get('Datos', 'exception_extension')
gw = config.get('Datos', 'default_gateway')

file_inbox = config.get('Datos', 'inbox')

def menuPrincipal():
	""" Esta es la definicio del menu principal """
	logger.info('Inicio del sistema, Menu principal.')
	salir = False
	while not salir:
		primerMenu = Menu.Menu("slGTD 0.1",
							"Sistema de Administración de Tareas.",
							("INBOX",
								"Próximo",
								"Proyectos",
								"En espera",
								"Algún día",
								"salir"),
							formulario)
		rta = primerMenu.mostrarMenu()
		if (rta == 0):
			logger.info('INBOX.')
			exit_sub_menu = False
			while not exit_sub_menu:
				inboxMenu = Ventana.Ventana(file_inbox,
										"INBOX | slGTD",
										"Tareas.",
										formulario)
				rta3 = inboxMenu.mostrarListado()
				exit_sub_menu = True
		elif (rta == 1):
			logger.info('Administración de Dominios.')
			exit_sub_menu = False
			while not exit_sub_menu:
				auxMenu = Menu.Menu("slGuardian | Administrar Dominios",
								"Administración de Dominios",
								("Bloquear Dominios",
								"Liberar Dominios",
								"Volver"),
								formulario)
				rta2 = auxMenu.mostrarMenu()
				if (rta2 == 0):
					segundoMenu = Ventana.Ventana(path_banned_site,
											"slGuardian | Listado de Dominios",
											"Dominios bloqueados.",
											formulario)
					rta3 = segundoMenu.mostrarListado()
				elif (rta2 == 1):
					segundoMenu = Ventana.Ventana(path_exception_site,
											"slGuardian | Listado de Dominios",
											"Dominios liberados.",
											formulario)
					rta3 = segundoMenu.mostrarListado()
				elif (rta2 == 2):
					exit_sub_menu = True
		elif (rta == 2):
			logger.info('Administración de Extensiones.')
			exit_sub_menu = False
			while not exit_sub_menu:
				auxMenu = Menu.Menu("slGuardian | Administrar Extensiones",
								"Administración de Extensiones en Archivos",
								("Bloquear Extensiones",
								"Liberar Extensiones",
								"Volver"),
								formulario)
				rta2 = auxMenu.mostrarMenu()
				if (rta2 == 0):
					segundoMenu = Ventana.Ventana(path_banned_extension,
											"slGuardian | Listado de Extensiones",
											"Extensiones bloqueadas.",
											formulario)
					rta3 = segundoMenu.mostrarListado()
				elif (rta2 == 1):
					segundoMenu = Ventana.Ventana(path_exception_extension,
											"slGuardian | Listado de Extensiones",
											"Extensiones liberadas.",
											formulario)
					rta3 = segundoMenu.mostrarListado()
				elif (rta2 == 2):
					exit_sub_menu = True
		elif (rta == 3):
			logger.info('Herramientas del sistema.')
			exit_sub_menu = False
			while not exit_sub_menu:
				auxMenu = Menu.Menu("slGuardian | Herramientas",
								"Herramientas de Sistema",
								("Configuraciones",
								"Verificar Conexion",
								"Volver"),
								formulario)
				rta2 = auxMenu.mostrarMenu()
				if (rta2 == 0):
					segundoMenu = Configuracion.VentanaConfiguracion(os.getcwd() + '/config/guardian.cnf',
														'slGuardian | Configuracion',
														'Configuración de Archivos',
														formulario)
					segundoMenu.modificarConfiguracion()
				elif (rta2 == 1):
					if (gw != ""):
						ping.verbose_ping(gw)
					ping.verbose_ping("google.com")
				elif (rta2 == 2):
					exit_sub_menu = True
		elif (rta == 5):
			logger.info('Finalización del sistema.')
			salir = True
		elif (rta == None):
			logger.info('Finalización del sistema.')
			salir = True
		else:
			logger.error('Operación no válida.')


if __name__ == '__main__':
	formulario = snack.SnackScreen()
	menuPrincipal()
	formulario.finish()
