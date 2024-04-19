import re
import os
import fnmatch

def buscarArchivo(ruta):
    for directorio, subdirectorios, archivos in os.walk(ruta):
        for archivo in fnmatch.filter(archivos, 'build.gradle'):
            return os.path.join(directorio, archivo)  # Retorna la primera coincidencia
    return None  # Si el archivo no se encuentra


# Función que busca los módulos en un archivo gradle y los cambia
def cambiarDependencias(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            content = file.read()

            # Patrón para capturar las dependencias
            patron = r"(implementation|androidTestImplementation) 'com.genexus.android:(.*?):(.*?)'"

            # Función de reemplazo para modificar las líneas de dependencia
            def reemplazar(match):
                modulo, version = match.group(2), match.group(3)
                new_line = f"{match.group(1)} project(':{modulo}')"
                print(f"Se modifica {match.group(0)} por: {new_line}")
                return new_line

            # Reemplazar las dependencias
            content = re.sub(patron, reemplazar, content)

            # Escribir el contenido modificado de vuelta al archivo
            with open(archivo, "w", encoding="utf-8") as file:
                file.write(content)

            print("Archivo modificado con éxito")
    except Exception as e:
        print("Error al abrir o modificar el archivo:", e)



