def calcular_reajuste(salario):
    percentual_aumento = 0
    aumento = 0

    if salario <= 280:
        percentual_aumento = 20
    elif 280 < salario <= 700:
        percentual_aumento = 15
    elif 700 < salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = salario * (percentual_aumento / 100)
    novo_salario = salario + aumento
    aumento_real = aumento - (aumento * 0.038)  # Descontando a inflação de 3.8%

    return percentual_aumento, aumento, novo_salario, aumento_real


if __name__ == "__main__":
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))
    percentual, aumento, novo_salario, aumento_real = calcular_reajuste(salario_atual)

    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: R$ {aumento_real:.2f}")
