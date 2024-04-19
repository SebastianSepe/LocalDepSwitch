from TrasnformGradle import buscarArchivo, cambiarDependencias

#ruta = "D:/GeneXus/Models/TestAccesibilidad/NETSQLServer1010/mobile/Android/TestMainMUX/"
def main():
    ruta = input("Ingrese la ruta del proyecto: ")
    archivo = buscarArchivo(ruta)
    if archivo:
        cambiarDependencias(archivo)
    else:
        print("No se encontró el archivo build.gradle")

if __name__ == "__main__":
    main()