import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QDesktopWidget, QMenuBar, QMenu, QMessageBox
)


# Función para calcular costos
def calcular_costo():
    try:
        # Obtener valores de entrada
        precio_material_total = float(campo_precio_total.text())
        peso_total_material = float(campo_peso_total.text())
        peso_usado = float(campo_peso_usado.text())
        horas = int(campo_horas.text())
        minutos = int(campo_minutos.text())
        margen = float(campo_margen.text())
        descuento = float(campo_descuento.text())

        # Tarifas fijas
        TARIFA_HORA = 100  # MXN por hora de impresión
        MANO_OBRA = 50  # MXN fijo por preparación/postprocesamiento
        GANANCIA_FIJA = 1.3  # Ganancia fija en porcentaje

        # Calcular costo del material usado
        costo_material_usado = (peso_usado / peso_total_material) * precio_material_total

        # Calcular costo del tiempo de impresión
        tiempo_total_horas = horas + (minutos / 60)
        costo_tiempo = tiempo_total_horas * TARIFA_HORA

        # Calcular costo total sin márgenes ni descuentos
        costo_base = costo_material_usado + costo_tiempo + MANO_OBRA

        # Aplicar margen de ganancia y descuento
        costo_con_margen = costo_base * (1 + margen / 100)
        costo_final = costo_con_margen * (1 - descuento / 100) * GANANCIA_FIJA

        # Mostrar el resultado
        resultado.setText(f"Costo total: ${round(costo_final, 2)} MXN")
    except ValueError:
        resultado.setText("Por favor, ingresa valores válidos.")


# Función para mostrar información del desarrollador
def mostrar_informacion():
    """
    Muestra información de ayuda en un cuadro de diálogo.
    """
    QMessageBox.information(
        ventana,
        "Acerca del Programa",
        "Calculadora de Impresión 3D\n"
        "Versión: 1.0\n"
        "Desarrollador: Nahum Flores\n"
        "Correo: excalibur_965@hotmail.com\n"
    )


# Crear la aplicación
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Calculadora de Impresión 3D")

# Establecer tamaño inicial de la ventana
ventana.resize(500, 400)

# Crear menú de ayuda
menu_bar = QMenuBar(ventana)
menu_ayuda = QMenu("Ayuda", ventana)
menu_ayuda.addAction("Acerca del programa", mostrar_informacion)
menu_bar.addMenu(menu_ayuda)

# Establecer el menú en la ventana
ventana.layout = QVBoxLayout()  # Diseño principal
ventana.layout.setMenuBar(menu_bar)  # Añadir menú sin que afecte el contenido

# Crear diseño vertical principal
layout = QVBoxLayout()

# Agregar campos de entrada
layout.addWidget(QLabel("Precio total del material (MXN):"))
campo_precio_total = QLineEdit()
layout.addWidget(campo_precio_total)

layout.addWidget(QLabel("Peso total del material (gramos):"))
campo_peso_total = QLineEdit()
layout.addWidget(campo_peso_total)

layout.addWidget(QLabel("Peso usado (gramos):"))
campo_peso_usado = QLineEdit()
layout.addWidget(campo_peso_usado)

layout.addWidget(QLabel("Horas de impresión:"))
campo_horas = QLineEdit()
layout.addWidget(campo_horas)

layout.addWidget(QLabel("Minutos de impresión:"))
campo_minutos = QLineEdit()
layout.addWidget(campo_minutos)

layout.addWidget(QLabel("Margen de ganancia (%):"))
campo_margen = QLineEdit()
campo_margen.setText("20")  # Margen predeterminado
layout.addWidget(campo_margen)

layout.addWidget(QLabel("Descuento (%):"))
campo_descuento = QLineEdit()
campo_descuento.setText("0")  # Descuento predeterminado
layout.addWidget(campo_descuento)

# Botón de cálculo
boton_calcular = QPushButton("Calcular costo")
boton_calcular.clicked.connect(calcular_costo)
layout.addWidget(boton_calcular)

# Resultado
resultado = QLabel("")
layout.addWidget(resultado)

# Añadir el diseño principal a la ventana
ventana.layout.addLayout(layout)
ventana.setLayout(ventana.layout)

# Centrar la ventana en la pantalla
pantalla = QDesktopWidget().screenGeometry()
tamaño_ventana = ventana.frameGeometry()
ventana.move(
    int((pantalla.width() - tamaño_ventana.width()) / 2),
    int((pantalla.height() - tamaño_ventana.height()) / 2)
)

# Mostrar la ventana
ventana.show()
sys.exit(app.exec_())
