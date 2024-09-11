import json
def analise_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    faturamentos = [item["valor"] for item in dados if item["valor"] > 0]
    faturamento_total = sum(faturamentos)
    media_mensal = faturamento_total/len(faturamentos)
    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    dias_acima_media = sum(1 for item in dados if item["valor"] > media_mensal)
    return menor_valor, maior_valor, dias_acima_media

menor, maior, dias_acima = analise_faturamento('valores.json')

print(f"O maior faturamento ocorrido em um dia foi de R$ {maior:.2f}")
print(f"O menor faturamento ocorrido em um dia foi de R$ {menor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")

