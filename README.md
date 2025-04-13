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


---

Actualizaciones de la versión 1.0.1 en la Calculadora de Impresión 3D
==========================================================

1. Funcionalidad para Guardar Datos
-----------------------------------
La calculadora ahora permite guardar todos los datos ingresados y el resultado calculado en un archivo de texto, lo que agrega una gran utilidad para registrar detalles de las impresiones 3D.

- **Detalles Guardados**:
  - Precio total del material.
  - Peso total del material.
  - Peso utilizado.
  - Tiempo de impresión (horas y minutos).
  - Margen de ganancia.
  - Descuento aplicado.
  - Costo total calculado.

- **Ubicación del Archivo**:
  - El archivo se genera automáticamente en la misma carpeta donde se encuentra el programa con el nombre `datos_impresion.txt`.

- **Cómo Usarlo**:
  1. Ingresa los datos necesarios.
  2. Haz clic en "Calcular costo" para generar el resultado.
  3. Haz clic en "Guardar datos" para registrar toda la información en el archivo de texto.

2. Interfaz Gráfica Mejorada
----------------------------
Se han realizado mejoras significativas en la apariencia y funcionalidad de la interfaz gráfica para brindar una experiencia de usuario más moderna y profesional.

- **Estilo Moderno con QSS**:
  - Fondos suaves en tonos claros con textos legibles.
  - Botones llamativos con efecto hover para destacar interacciones.
  - Uniformidad en los campos de entrada con bordes redondeados y espaciados adecuados.

- **Organización**:
  - Título visualmente destacado con colores llamativos.
  - Disposición limpia y centrada para una experiencia más intuitiva.

- **Menú "Ayuda" Mejorado**:
  - Información clara sobre el programa y detalles del desarrollador.
  - Accesible desde la barra superior para mayor facilidad.

Beneficios para el Usuario
---------------------------
1. **Guardar Datos en un Archivo**:
   - Ideal para mantener un registro de costos en distintos proyectos de impresión.
   - Facilita la consulta y el análisis de los datos ingresados y resultados calculados.

2. **Interfaz más Profesional**:
   - Mejora la interacción gracias a un diseño intuitivo y visualmente atractivo.
   - Hace que la herramienta sea más fácil y agradable de utilizar.

Estas mejoras hacen que la Calculadora de Impresión 3D sea más completa y funcional para los usuarios interesados en optimizar sus proyectos de impresión.
