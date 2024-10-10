#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;



import json 

with open('dados/dados.json') as f: 
    faturamento = json.load(f)


valores = [dia['valor'] for dia in faturamento if dia ['valor']>0]

media_mensal = sum(valores)/ len(valores)
maior_valor = max(valores)
menor_valor = min(valores)

dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"O maior valor de faturamento é: {maior_valor:.2f}")
print(f"Menor valor de faturamento é: {menor_valor:.2f}")
print(f"Número de dias com faturamento maior que a média é: {dias_acima_da_media}")


#Executando o códico consultando o arquivo "dados.json"
#Teremos que o maior valor de faturamento será: 48924.24
#Menor valor de faturamento será: 373.78
#E o número de dias com faturamento maior que a média será: 10