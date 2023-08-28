# QueSignifica
Un pequeño programa escrito en Python para buscar el significado de una palabra.

Escrito para practicar el lenguaje Python a nivel básico.

"QueSignifica" hace uso del módulo **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)**, creado por *Leonard Richardson* y de **[wxWidgets](https://www.wxwidgets.org/)** a través del módulo **[wxPython](https://wxpython.org/index.html)** para la interfaz gráfica.

Con está mini aplicación pongo en práctica el uso de **urllib** para el acceso y utilización de los recursos de Internet __URL__.
La aplicación simplemente toma una variable _str_ y la incluye en otra cadena que es la URL de la **Real Academia Española** para realizar la consulta y mostrar el resultado.
Me he visto frustrado temporalmente por los problemas con el unicode y las letras especiales con acentos y eñes aunque al final se ha podido solucionar con una simple línea:
```palabra = quote(palabra)```

También ha sido mi primera toma de contacto con wxWidgets utilizando **[wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder)** para crear la interfaz gráfica.

Para la creación del ejecutable he utilizado **PyInstaller** y aunque me hubiese gustado no he sabido integrar el icono de la aplicación en el propio ejecutable para no depender de un archivo suelto.

Soy consciente de que el código no está ni de lejos optimizado y que el ejecutable tiene un peso enorme pero mi prioridad es que funcionase.
