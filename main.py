print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
cobertura = metros_quadrados/3
latas = 1
valor = 80
if cobertura > 18:
    latas = int(cobertura / 18) + 1
    valor = valor * latas
if cobertura < 18:
    latas = 1
    valor = valor * latas
if cobertura == 0:
    latas = 0
    valor = 0

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = latas
valor_total = valor

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")