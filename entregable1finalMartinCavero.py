import numpy as np

def ingresar_matriz(nombre, filas, columnas):
    """Solicita al usuario una matriz con dimensiones específicas."""
    print(f"\n👉 Ingrese la matriz {nombre} de tamaño {filas}x{columnas}")
    matriz = []
    for i in range(filas):
        while True:
            fila_str = input(f"Fila {i+1}: ")
            try:
                fila = [float(x.strip()) for x in fila_str.split(',') if x.strip()]
                if len(fila) != columnas:
                    print(f"❌ Debes ingresar exactamente {columnas} valores.")
                else:
                    matriz.append(fila)
                    break
            except ValueError:
                print("❌ Entrada inválida. Usa solo números.")
    return np.array(matriz)

def solicitar_matrices_iguales():
    """Solicita matrices A, B y C con mismas dimensiones y compatibles para A @ B @ C."""
    while True:
        try:
            filas = int(input("📌 Número de filas para matrices A, B y C: "))
            columnas = int(input("📌 Número de columnas para matrices A, B y C: "))

            if filas <= 0 or columnas <= 0:
                print("❌ Las dimensiones deben ser mayores que cero.")
                continue

            # Validación de compatibilidad para A @ B @ C
            if columnas != filas:
                print("❌ Para A @ B @ C, las columnas deben coincidir con filas (columnas == filas).")
                print("🔁 Intenta nuevamente.")
                continue

            A = ingresar_matriz("A", filas, columnas)
            B = ingresar_matriz("B", filas, columnas)
            C = ingresar_matriz("C", filas, columnas)

            return A, B, C
        except ValueError:
            print("❌ Entrada inválida.")

# ----------------------------------
# FUNCIONES DE PROPIEDADES
# ----------------------------------

def comprobar_suma(A, B, C):
    print("\n--- PROPIEDADES DE LA SUMA ---")
    print("A + B:\n", A + B)
    print("B + A:\n", B + A)
    print("✅ Conmutativa:", np.allclose(A + B, B + A))

    print("\n(A + B) + C:\n", (A + B) + C)
    print("A + (B + C):\n", A + (B + C))
    print("✅ Asociativa:", np.allclose((A + B) + C, A + (B + C)))

    print("\nA + (-A):\n", A + (-A))
    print("✅ Inverso suma:", np.allclose(A + (-A), np.zeros_like(A)))

def comprobar_multiplicacion(A, B, C):
    print("\n--- PROPIEDADES DE LA MULTIPLICACIÓN ---")

    print("\n(A @ B) @ C:\n", (A @ B) @ C)
    print("A @ (B @ C):\n", A @ (B @ C))
    print("✅ Asociativa:", np.allclose((A @ B) @ C, A @ (B @ C)))

    print("\nVerificando distributiva:")
    try:
        if B.shape != C.shape:
            raise ValueError("❌ B y C deben tener la misma forma para sumarse.")
        print("A @ (B + C):\n", A @ (B + C))
        print("A @ B + A @ C:\n", A @ B + A @ C)
        print("✅ Distributiva:", np.allclose(A @ (B + C), A @ B + A @ C))
    except Exception as e:
        print(f"⚠️ Distributiva no evaluada: {e}")

    print("\nVerificando inversa (si aplica):")
    for matriz, nombre in zip([A, B, C], ["A", "B", "C"]):
        try:
            if matriz.shape[0] == matriz.shape[1]:
                inversa = np.linalg.inv(matriz)
                identidad = np.eye(matriz.shape[0])
                print(f"{nombre} @ {nombre}⁻¹:\n", matriz @ inversa)
                print("✅ Inversa:", np.allclose(matriz @ inversa, identidad))
            else:
                print(f"⚠️ {nombre} no es cuadrada. No se puede calcular inversa.")
        except np.linalg.LinAlgError:
            print(f"⚠️ La matriz {nombre} no tiene inversa (singular).")

# ----------------------------------
# EJECUCIÓN PRINCIPAL
# ----------------------------------

if __name__ == "__main__":
    print("=== MATRICES PARA SUMA Y MULTIPLICACIÓN ===")
    A, B, C = solicitar_matrices_iguales()

    comprobar_suma(A, B, C)
    comprobar_multiplicacion(A, B, C)

    print("\n✅ ¡Programa finalizado correctamente!")
