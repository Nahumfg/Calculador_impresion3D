def calcular_costo_impresion(precio_material_total, peso_total_material, peso_usado, horas, minutos, margen=20):
    """
    Calcula el costo total de impresión 3D, considerando el material gastado y tarifas fijas.

    Parámetros:
    - precio_material_total: Precio total del material en MXN (como el rollo completo).
    - peso_total_material: Peso total del material en gramos (por ejemplo, 1000g para 1 kg).
    - peso_usado: Peso del material usado en gramos.
    - horas: Tiempo de impresión en horas.
    - minutos: Tiempo de impresión en minutos.
    - margen: Margen de ganancia en porcentaje (opcional, por defecto 20%).

    Tarifas fijas:
    - Tarifa por hora de impresión: $100 MXN.
    - Mano de obra fija: $50 MXN.

    Retorna:
    - Costo total en pesos mexicanos.
    """
    # Tarifas fijas
    TARIFA_HORA = 100  # MXN por hora de impresión
    MANO_OBRA = 50  # MXN fijo por preparación/postprocesamiento

    # Costo del material usado
    costo_material_usado = (peso_usado / peso_total_material) * precio_material_total

    # Costo del tiempo de impresión
    tiempo_total_horas = horas + (minutos / 60)
    costo_tiempo = tiempo_total_horas * TARIFA_HORA

    # Costo total
    costo_total = (costo_material_usado + costo_tiempo + MANO_OBRA) * (1 + margen / 100)
    return round(costo_total, 2)

# Ejemplo de uso
# Datos manuales
precio_material_total = float(input("Ingresa el precio total del material en MXN (por ejemplo, un rollo): "))
peso_total_material = float(input("Ingresa el peso total del material en gramos (por ejemplo, 1000g): "))
peso_usado = float(input("Ingresa el peso del material usado en gramos: "))
horas = int(input("Ingresa las horas de impresión: "))
minutos = int(input("Ingresa los minutos de impresión: "))
margen = float(input("Ingresa el margen de ganancia (opcional, %): ") or 20)

costo = calcular_costo_impresion(precio_material_total, peso_total_material, peso_usado, horas, minutos, margen)
print(f"Costo total: ${costo} MXN")