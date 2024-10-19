import json

def calcular_faturamento(faturamentos):
    f_real = [dia['faturamento'] for dia in faturamentos if dia['faturamento'] > 0]

    if len(f_real) == 0:
        return "Não há faturamentos válidos para calcular."

    menor_f = min(f_real)
    maior_f= max(f_real)
    media_mensal = sum(f_real) / len(f_real)
    dias_acima = sum(1 for dia in f_real if dia > media_mensal)

    return menor_f, maior_f, dias_acima



with open('faturamento.json', 'r') as file:
    faturamentos = json.load(file)

menor, maior, dias_acima = calcular_faturamento(faturamentos)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
