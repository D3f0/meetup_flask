# Ejemplo de intoducción a Flask

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/D3f0/meetup_flask?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![Logo Flask](http://flask.pocoo.org/docs/0.10/_images/logo-full.png)


Las fliminas (que vimos las primeras nomás, pero pueden servir de guía): https://speakerdeck.com/miguelgrinberg/flask-workshop

# Instalación

Para instalar flask:

```bash
pip install Flask
```

(Si no tenemos `pip`, bajarlo de [aquí](https://bootstrap.pypa.io/get-pip.py) y ejecutar `python get-pip.py`)


# Ejecución

```bash
python runserver.py
```

Luego abrir el navegador en http://127.0.0.1:5000/

# Vistas (o páginas)

Ejemplo en https://github.com/D3f0/meetup_flask/blob/master/runserver.py#L8-L14

# Templates

Plantillas, ejemplo [base.html](./templates/base.html)

# Archivos estáticos 

Es el código JavaScript, estilo CSS, Imágens, Vídeo, Imágenes que incluimos en la página.

Se ubica en [`static`](./static/)

# Documentación

La documentación de Flask se encuentra en http://flask.pocoo.org/docs/0.10/

# Documentación formato Online

Con [Zeal](http://zealdocs.org/) para Windows y Linu (Dash en OSX) pueden descargarse la documentación offline Python, Flask, CSS, HTML, etc.

Desde el menú Opciones, en Docsets se deben descargar primero las documentaciones que nos interesen. Ver capturas de pantalla más abajo.

![Imagen](./doc/zeal1.png)
![Imagen](./doc/zeal2.png)
