# -*- coding: utf-8 -*-

import wx, wx.xrc
import urllib.request, urllib.parse, urllib.error
from urllib.parse import quote
from bs4 import BeautifulSoup

agente = 'Mozilla/5.0'
palabra = ''

class mainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u'QuéSignifica', pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU )

		self.SetIcon(icono)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonBuscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttonBuscar.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2.Add( self.buttonBuscar, 0, wx.ALL, 5 )

		self.textPalabra = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,27 ), wx.TE_PROCESS_ENTER )
		self.textPalabra.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2.Add( self.textPalabra, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, 0, 5 )

		self.textDescripcion = wx.TextCtrl( self, wx.ID_ANY, u"Descripción", wx.Point( -1,-1 ), wx.Size( -1,250 ), wx.TE_READONLY | wx.TE_MULTILINE )
		self.textDescripcion.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.textDescripcion, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.buttonBuscar.Bind( wx.EVT_BUTTON, self.clickBuscar )
		self.textPalabra.Bind( wx.EVT_TEXT, self.textUpdated )
		self.textPalabra.Bind( wx.EVT_TEXT_ENTER, self.enterPressed )

	def __del__( self ):
		pass

	def clickBuscar( self, event ):
		palabra = self.textPalabra.GetValue()
		palabra = quote(palabra) # para lidiar con el unicode de las narices

		if len(palabra) < 1 :
			self.textDescripcion.Clear()
			self.textDescripcion.AppendText('Escriba una palabra para saber su significado.')
		else:
			url_in = f'https://dle.rae.es/?formList=form&w={palabra}#'
			url_request = urllib.request.Request(url_in, None, headers={'User-Agent': agente})
			try:
				url_open = urllib.request.urlopen(url_request).read()
			except UnicodeEncodeError as unierror:
				unierror = str(unierror)
				self.textDescripcion.Clear()
				self.textDescripcion.AppendText(f'Se ha producido el siguiente error:\n{unierror}')
			soup = BeautifulSoup(url_open, 'html.parser')
			metas = soup('meta')

			for meta in metas:
				nombre = meta.get('name', None)
				contenido = meta.get('content', None)
				
				if nombre == 'description' :
					if contenido.startswith('Versión electrónica') :
						self.textDescripcion.Clear()
						self.textDescripcion.AppendText(f'La palabra "{palabra}" no se encuentra en el diccionario de la RAE.')
					else :
						self.textDescripcion.Clear()
						self.textDescripcion.AppendText(contenido)

		event.Skip()

	def textUpdated( self, event ):
		event.Skip()

	def enterPressed( self, event ):
		palabra = self.textPalabra.GetValue()
		palabra = quote(palabra)

		if len(palabra) < 1 :
			self.textDescripcion.Clear()
			self.textDescripcion.AppendText('Introduzca una palabra a buscar')
		else:
			url_in = f'https://dle.rae.es/?formList=form&w={palabra}#'
			url_request = urllib.request.Request(url_in, None, headers={'User-Agent': agente})
			try:
				url_open = urllib.request.urlopen(url_request).read()
			except UnicodeEncodeError as unierror:
				unierror = str(unierror)
				self.textDescripcion.Clear()
				self.textDescripcion.AppendText(f'Se ha producido el siguiente error:\n{unierror}')
			soup = BeautifulSoup(url_open, 'html.parser')
			metas = soup('meta')

			for meta in metas:
				nombre = meta.get('name', None)
				contenido = meta.get('content', None)
				
				if nombre == 'description' :
					if contenido.startswith('Versión electrónica') :
						self.textDescripcion.Clear()
						self.textDescripcion.AppendText(f'La palabra "{palabra}" no se encuentra en el diccionario de la RAE.')
					else :
						self.textDescripcion.Clear()
						self.textDescripcion.AppendText(contenido)

		event.Skip()

app = wx.App()
icono = wx.EmptyIcon()
icono.CopyFromBitmap(wx.Bitmap('rae.ico', wx.BITMAP_TYPE_ICO))
frame = mainFrame(None)
frame.Show()
app.MainLoop()
