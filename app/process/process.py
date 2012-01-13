#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import gettext

try:
	from snack import *
except ImportError:
	print gettext.gettext('newt library not installed')


class Process:
	def __init__(self, nameFile, title, text, screen=None):
		self.nameFile = nameFile
		self.title = title
		self.text = text
		self.screen = screen
		if (title == ""):
			self.title = gettext.gettext("No Title")

	def readFile(self):
		if os.path.exists(self.nameFile):
			self.fileInput = open(self.nameFile, "r")
			self.lineFile = self.fileInput.readlines()
			self.fileInput.close()
		else:
			self.lineFile = gettext.gettext("No Record")
		return self.lineFile

	def showProcess(self):
		self.nextItem = readFile()
		exit = False
		while not exit:
			print hola
			exit = True