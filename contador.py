import collections
conteo_municipios = collections.Counter()

try:
    # Abrimos el archivo para leerlo.
    with open('where.data', 'r', encoding='utf-8') as archivo:
        # Bucle 'for' para leer cada línea del archivo.
        for linea in archivo:
            # Quitamos espacios y saltos de línea.
            linea_limpia = linea.strip()
            if linea_limpia:
                # Dividimos la línea por las comas.
                partes = linea_limpia.split(',')
                # Verificamos que la línea tenga al menos 3 columnas.
                if len(partes) >= 1:
                    # Obtenemos la tercera columna (índice 2) y quitamos espacios.
                    municipio = partes[1].strip()
                    # Agregamos al contador.
                    conteo_municipios[municipio] += 1

    # Imprimimos los resultados.
    print("Conteo de repeticiones por municipio/alcaldía:")
    for municipio, cantidad in conteo_municipios.items():
        print(f"- {municipio}: {cantidad}")

except FileNotFoundError:
    print("Error: No se encontró el archivo 'where.data'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")