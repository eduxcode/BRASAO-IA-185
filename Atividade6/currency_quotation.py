import requests
import datetime

def get_currency_quotation(currency_code):
    url = f"https://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    while True:
        currency_code_input = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
        if len(currency_code_input) == 3 and currency_code_input.isalpha():
            break
        else:
            print("Código de moeda inválido. Por favor, digite um código de 3 letras (ex: USD).")

    quotation_data = get_currency_quotation(currency_code_input)

    if quotation_data:
        key = f"{currency_code_input}BRL"
        if key in quotation_data:
            currency_info = quotation_data[key]
            timestamp = int(currency_info["timestamp"])
            last_update = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            print(f"\nCotação de {currency_code_input}/BRL:")
            print("Valor Atual (Compra):	", currency_info["bid"])
            print("Valor Máximo:	\t", currency_info["high"])
            print("Valor Mínimo:	\t", currency_info["low"])
            print("Última Atualização:	", last_update)
        else:
            print(f"Não foi possível encontrar a cotação para {currency_code_input}.")
    else:
        print("Erro ao consultar a API. Verifique sua conexão ou tente novamente mais tarde.")
