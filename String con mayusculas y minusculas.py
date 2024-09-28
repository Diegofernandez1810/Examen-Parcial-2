def contar_a_A(cadena: str) -> tuple:
    a_min = cadena.count('a')
    a_may = cadena.count('A')
    
    return a_min, a_may


texto = "Diego Alejandro Fernandez Gonzalez"
a_min, a_may = contar_a_A(texto)
print(f"Cantidad de 'a': {a_min}, Cantidad de 'A': {a_may}")

