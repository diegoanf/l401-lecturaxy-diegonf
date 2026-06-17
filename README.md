# Visualización de Datos X-Y con Flask

## Alumno

Diego Alonso Núñez Falcon

## Correo

[diegoxdd2000@gmail.com](mailto:diegoxdd2000@gmail.com)

## Descripción

Proyecto desarrollado para la asignatura Desarrollo de Software para Hardware.

La aplicación recibe datos de los ejes X e Y desde una aplicación móvil mediante una conexión TCP. Los valores se muestran en una aplicación web creada con Flask y se representan también en una matriz de posición 4×4.

## Objetivos

* Recibir datos X e Y desde una aplicación móvil.
* Mostrar los valores numéricos en una página web.
* Actualizar la información automáticamente sin utilizar JavaScript.
* Escalar las lecturas a coordenadas dentro de una matriz 4×4.
* Encender la celda correspondiente a la posición X-Y.
* Permitir la navegación entre la vista de valores y la vista de matriz.

## Tecnologías utilizadas

* Python 3
* Flask
* HTML5
* CSS3
* Jinja2
* Sockets TCP
* Git y GitHub

## Restricciones consideradas

* No se utiliza JavaScript.
* No se utiliza la etiqueta script.
* El CSS está definido dentro de la etiqueta head.
* Las referencias CSS utilizan identificadores id.
* La APK no se almacena en el repositorio personal.

## Estructura del proyecto

```
.
├── app.py
├── README.md
├── templates
│   ├── index.html
│   └── matrix.html
└── capturas
    ├── vista-principal.png
    └── vista-matriz.png
```

## Funcionamiento

La ruta principal muestra los valores actuales de X e Y.

La ruta `/matrix` transforma los valores recibidos, cuyo rango esperado se encuentra aproximadamente entre -10 y 10, en coordenadas enteras entre 0 y 3.

La matriz contiene 16 celdas. La celda correspondiente a la posición calculada se ilumina en color verde.

## Ejecución

Activar el entorno virtual:

```
source entorno-l401/bin/activate
```

Ejecutar Flask:

```
python app.py
```

Abrir en el navegador:

```
http://127.0.0.1:8080
```

Vista de la matriz:

```
http://127.0.0.1:8080/matrix
```

## Referencias

* Repositorio base proporcionado por el docente.
* Referencia de estructura y representación: `schweineorgel/l401-lecturaxy`.

## Autor

Diego Alonso Núñez Falcon
Desarrollo de Software para Hardware
