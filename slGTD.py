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
import gettext

import app.default.menu as Menu
import app.default.ventana as Ventana
import app.config.ventanaconfig as Configuracion

try:
	from snack import *
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

file_inbox = config.get('Datos', 'inbox')

def menuPrincipal():
	logger.info('Inicio del sistema, Menu principal.')
	exit = False
	while not exit:
		bb = ButtonBar(formulario, (("Recopilar", "recopilar"),
								("Procesar", "procesar"),
								("Organizar", "organizar"),
								("Revisar", "revisar"),
								("Salir", "salir"))
								)
		g = GridForm(formulario, "slGTD 0.1", 1, 3)
		g.add(bb, 0, 0, (2, 2, 2, 2))
	
		resultado = g.runOnce()
		if (bb.buttonPressed(resultado) == "recopilar"):
			inboxMenu = Ventana.Ventana(file_inbox,
									"INBOX | slGTD",
									"Tareas.",
									formulario)
			rta3 = inboxMenu.mostrarListado()
		elif (bb.buttonPressed(resultado) == "salir"):
			logger.info('Finalización del sistema.')
			exit = True
		else:
			logger.error('Operación no válida.')


if __name__ == '__main__':
	(l, c) = str.split(commands.getoutput('stty size'))
	(lineas, columnas) = (int(l), int(c))
	(lineas, columnas) = lineas or 24, columnas or 79
	formulario = SnackScreen()
	menuPrincipal()
	formulario.finish()
