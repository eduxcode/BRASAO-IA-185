def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calcula o preço final de um produto após a aplicação de um desconto.

    Parâmetros:
        original_price (float): O preço original do produto.
        discount_percentage (float): O percentual de desconto a ser aplicado (ex: 10 para 10%).

    Retorna:
        float: O preço final do produto após o desconto.
    """
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

if __name__ == "__main__":
    try:
        price_input = input("Informe o preço original do produto (ex: 250.75): ")
        product_price = float(price_input)

        discount_input = input("Informe o percentual de desconto (ex: 10): ")
        discount_percent = float(discount_input)

        if product_price < 0 or discount_percent < 0 or discount_percent > 100:
            print("Valores inválidos. O preço e a porcentagem de desconto devem ser positivos, e a porcentagem de desconto não pode exceder 100.")
        else:
            final_price_calculated = calculate_discounted_price(product_price, discount_percent)
            print(f"Preço original: R${product_price:.2f}")
            print(f"Percentual de desconto: {discount_percent:.2f}%")
            print(f"Preço final após desconto: R${final_price_calculated:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para o preço e o percentual de desconto.")
