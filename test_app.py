from app import calcular_autonomia

def test_calculo_correcto():
    # Verificamos si la función hace la matemática bien
    assert calcular_autonomia(10, 15) == 150
    print("¡Prueba unitaria aprobada con éxito!")

if __name__ == "__main__":
    test_calculo_correcto()