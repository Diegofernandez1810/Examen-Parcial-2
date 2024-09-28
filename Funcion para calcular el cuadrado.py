def calcular_cuadrado():
    numero = int(input("Ingresa un número entero: "))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")


def calcular_producto():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es {producto}")

def main():
    calcular_cuadrado()
    
    calcular_producto()

if __name__ == "__main__":
    main()
