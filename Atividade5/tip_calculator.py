def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula a gorjeta a ser deixada em um restaurante.
    
    """
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

if __name__ == "__main__":
    # Exemplo de uso
    conta = 100.00
    gorjeta_percentual = 15
    gorjeta_calculada = calcular_gorjeta(conta, gorjeta_percentual)
    print(f"Valor da conta: R${conta:.2f}")
    print(f"Porcentagem da gorjeta: {gorjeta_percentual}%")
    print(f"Valor da gorjeta: R${gorjeta_calculada:.2f}")

    conta_2 = 75.50
    gorjeta_percentual_2 = 20
    gorjeta_calculada_2 = calcular_gorjeta(conta_2, gorjeta_percentual_2)
    print(f"\nValor da conta: R${conta_2:.2f}")
    print(f"Porcentagem da gorjeta: {gorjeta_percentual_2}%")
    print(f"Valor da gorjeta: R${gorjeta_calculada_2:.2f}")
