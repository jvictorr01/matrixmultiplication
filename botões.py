#ista de botões e de camisas produzidas
botoes_p = [3, 1, 3]
botoes_g = [6, 5, 5]
camisas_maio = [100, 50, 50]
camisas_junho = [100, 50, 50]

#variaveis
total_botao_maio = 0
total_botao_junho = 0

#total de botões usados em maio
for i in range(len(botoes_p)):
    total_botao_maio += botoes_p[i] * camisas_maio[i]
    total_botao_maio += botoes_g[i] * camisas_maio[i]

#total de botões usados em junho
for i in range(len(botoes_p)):
    total_botao_junho += botoes_p[i] * camisas_junho[i]
    total_botao_junho += botoes_g[i] * camisas_junho[i]

#resultados
print("Total de botões usados em maio:", total_botao_maio)
print("Total de botões usados em junho:", total_botao_junho)