import sys
import subprocess
import pkg_resources

def verificar_instalar_librerias(librerias):
    """
    Verifica si las librerías están instaladas. Si no lo están, las instala.
    :param librerias: Lista de librerías a verificar e instalar.
    """
    librerias_faltantes = []

    # Verificar librerías instaladas
    for libreria in librerias:
        try:
            pkg_resources.require(libreria)
        except pkg_resources.DistributionNotFound:
            librerias_faltantes.append(libreria)
        except pkg_resources.VersionConflict as e:
            print(f"Conflicto de versión con {libreria}: {e}")

    # Instalar librerías faltantes
    if librerias_faltantes:
        print(f"Las siguientes librerías no están instaladas: {', '.join(librerias_faltantes)}")
        for libreria in librerias_faltantes:
            try:
                print(f"Instalando {libreria}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", libreria])
                print(f"Librería {libreria} instalada correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"Error al instalar {libreria}: {e}")
    else:
        print("Todas las librerías necesarias ya están instaladas.")

if __name__ == "__main__":
    # Lista de librerías necesarias
    librerias_necesarias = ["PyQt5", "Pillow"]

    print("Verificando e instalando dependencias necesarias...")
    verificar_instalar_librerias(librerias_necesarias)
    print("Finalizado.")