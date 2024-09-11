def percentual_representação(faturamento):
    faturamento_total = sum(faturamento.values())
    for estado, valor in faturamento.items():
        print(f"O estado de {estado} repressentou {(valor/faturamento_total)*100:.2f}% do faturamento total")



faturamento = {"SP": 67836.43,
"RJ": 36678.66,
"MG": 29229.88,
"ES": 27165.48,
"OUTROS":  19849.53}

percentual_representação(faturamento)






