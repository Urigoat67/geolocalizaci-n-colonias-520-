Proyecto de Geografía del CCH Oriente
Este proyecto utiliza Python y una API de geocodificación para visualizar en un mapa la ubicación de los compañeros del CCH Oriente, en los municipios y alcaldías de la zona oriente del Valle de México.

Descripción del Proyecto
El objetivo es geocodificar las direcciones (colonias y municipios) de un grupo de estudiantes para luego visualizarlas en un mapa interactivo. El proyecto está diseñado en dos partes:

Script de Python (geo_where.py): Se encarga de leer las direcciones de un archivo de texto (where.data), consultar la API de OpenCage Geocoding para obtener las coordenadas de latitud y longitud, y generar un archivo JavaScript (where.js) con los datos formateados.

Visualización en HTML: Un archivo HTML (where.html) consume el archivo where.js y usa una biblioteca de mapas (como Leaflet.js) para renderizar los puntos de geolocalización en un mapa dinámico.

Requisitos
Para ejecutar este proyecto, necesitas tener instalado:

Python 3.x

Una clave de API de OpenCage: Deberás registrarte en OpenCage Geocoding para obtener una clave de API gratuita y añadirla al script de Python.

Cómo Usar
Sigue estos pasos para geocodificar las direcciones y generar el mapa:

Prepara los datos:

Crea un archivo de texto llamado where.data en la carpeta opengeo.(tambien se puede adaptar el codigo para usar directamente alguna tabla de excel con los datos)

En este archivo, escribe cada dirección en una nueva línea, en el formato Colonia, Municipio o Alcaldía. Por ejemplo:

Los Héroes Chalco 3, Chalco de Díaz Covarrubias
Agrícola Oriental, Iztacalco

Configura el script:

Abre geo_where.py.

Asegúrate de que la variable api_key contenga tu clave de API de OpenCage.

Ejecuta el script:

Abre una terminal o línea de comandos.

Navega a la carpeta del proyecto.

Ejecuta el script con el comando:

python geo_where.py

El script imprimirá el progreso en la consola y generará el archivo where.js una vez que termine.

Visualiza el mapa:

Una vez que el script haya terminado de ejecutarse, abre el archivo where.html en tu navegador web para ver el mapa con las ubicaciones de tus compañeros.
