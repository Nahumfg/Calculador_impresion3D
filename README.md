# Calculadora de Impresión 3D

La **Calculadora de Impresión 3D** es una herramienta intuitiva y eficiente para calcular los costos asociados a proyectos de impresión 3D. Desarrollada en Python con una interfaz gráfica construida con PyQt5, esta herramienta permite a los usuarios calcular costos de materiales, tiempo de impresión, márgenes de ganancia y descuentos de manera sencilla.

## Funcionalidades principales

- **Cálculo de costos automatizado**: Introduce los datos necesarios y obtén un costo detallado.
- **Interfaz gráfica fácil de usar**: Diseñada para ser amigable e intuitiva.
- **Soporte para tarifas fijas**: Incluye costos predefinidos de mano de obra y tiempo de impresión.
- **Flexibilidad**: Permite ajustar márgenes de ganancia y aplicar descuentos personalizados.
- **Optimización para uso independiente y desarrollador**: Incluye un instalador (`instalador.py`) para verificar e instalar dependencias automáticamente.

---

## Requisitos

Antes de ejecutar el programa, asegúrate de que tu entorno cumpla con los siguientes requisitos:

- **Sistema operativo**: Windows, macOS o Linux.
- **Python 3.8 o superior**: Solo para desarrolladores que deseen usar el código fuente.
- **Librerías necesarias**:  
  - `PyQt5`
  - `Pillow`

Si usas el archivo ejecutable (`.exe`), no necesitas instalar Python ni las librerías. Solo asegúrate de agregar el `.exe` como excepción en tu antivirus (ver más abajo).

---

## Cómo usar el programa

### 1. Ejecutar como archivo `.exe`

Si no deseas usar el código fuente, simplemente ejecuta el archivo **`calculador_3d_GUI.exe`**.

#### ⚠ Instrucciones para evitar bloqueos del antivirus:

Debido a que el archivo `.exe` no cuenta con un certificado digital, algunos antivirus podrían bloquearlo. Sigue estos pasos para agregarlo como una excepción:

1. **Ubica el archivo ejecutable**:
   - Guarda el archivo `.exe` en una carpeta confiable de tu sistema.
2. **Abre tu antivirus**:
   - Busca la sección de "Configuración", "Exclusiones" o "Excepciones".
3. **Agrega la excepción**:
   - Selecciona la opción para agregar una nueva exclusión y elige el archivo `.exe` o la carpeta donde está almacenado.
4. **Confirma y guarda los cambios**:
   - Reinicia el programa antivirus si es necesario.

Ahora puedes ejecutar el archivo sin interrupciones.

---

### 2. Ejecutar desde el código fuente

Si prefieres trabajar con el código fuente:

1. Asegúrate de tener **Python 3.8 o superior** instalado.
2. Descarga el código fuente del repositorio.
3. Instala las dependencias necesarias:
   ```bash
   python -m pip install PyQt5 Pillow
