def calcular_autonomia(tanque, consumo_por_km):
    # Lógica simple: capacidad del tanque por lo que rinde
    return tanque * consumo_por_km

if __name__ == "__main__":
    print(f"Autonomía estimada: {calcular_autonomia(40, 15)} km")