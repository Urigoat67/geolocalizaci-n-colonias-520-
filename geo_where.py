import urllib.request, urllib.parse, urllib.error
import json
import time
import ssl
import codecs
#para usar este script nesecitas iniciar secion y obtener tu api key de opencage
# https://opencagedata.com/api
# Reemplaza 'TU_CLAVE_AQUI' con la clave que obtuviste de OpenCage
api_key = ""#tu_clave_aqui
serviceurl = 'https://api.opencagedata.com/geocode/v1/json?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Abrimos el JS de salida que consumirá el HTML
fout = codecs.open('where.js', 'w', 'utf-8')
fout.write("myData = [\n")
count = 0

# Lee cada línea de where.data (una dirección por línea)
with open('n.data', 'r', encoding='utf-8') as fh:
    for raw in fh:
        address = raw.strip()

        # Permite comentarios o líneas vacías
        if not address or address.startswith('#'):
            continue

        # Construye la URL con la nueva API y la clave
        parms = {'q': address, 'key': api_key}
        url = serviceurl + urllib.parse.urlencode(parms)
        print('Recuperando', url)

        try:
            uh = urllib.request.urlopen(url, context=ctx, timeout=30)
            data = uh.read().decode()
            print('Recuperados', len(data), 'caracteres')

            js = json.loads(data)

            # Revisa la estructura de la respuesta de OpenCage
            if 'results' not in js or not js['results']:
                print('==== No se encontró la ubicación ====:', address)
                continue

            lat = js['results'][0]['geometry']['lat']
            lng = js['results'][0]['geometry']['lng']
            where = js['results'][0]['formatted'].replace("'", "")

            print('Ubicación:', where, 'Lat:', lat, 'Lng:', lng)

            if count > 0:
                fout.write(",\n")
            # ESCRITURA EN where.js
            output = f"[{lat},{lng}, '{where}']"
            fout.write(output)
            count += 1

            # realentizar un poco las consultas de la api 
            if count % 10 == 0:
                print('Pausando un momento...')
                time.sleep(5)

            time.sleep(0.5)

        except Exception as e:
            print('Error al procesar la ubicación:', e)
            continue

# Cierra el arreglo JS
fout.write("\n];\n")
fout.close()

print("---")
print(count, "registros escritos en where.js")
print("Abre where.html para ver el mapa en tu navegador.")
