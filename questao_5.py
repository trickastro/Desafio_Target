def inverte(texto):
    invertida = ""

    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto = input("Digite uma string para inverter: ")
resultado = inverte(texto)
print(f"String invertida: {resultado}")
