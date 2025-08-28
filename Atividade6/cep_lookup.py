import requests

def lookup_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    while True:
        cep_input = input("Digite o CEP para consulta (apenas números): ")
        if cep_input.isdigit() and len(cep_input) == 8:
            break
        else:
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")

    address_data = lookup_cep(cep_input)

    if "erro" not in address_data:
        print("\nInformações do Endereço:")
        print("Logradouro:", address_data.get("logradouro"))
        print("Bairro:", address_data.get("bairro"))
        print("Cidade:", address_data.get("localidade"))
        print("Estado:", address_data.get("uf"))
    else:
        print("CEP não encontrado ou inválido.")
