import csv

def create_personal_data_csv(filename="personal_data.csv"):
    data = [
        ["Nome", "Idade", "Cidade"],
        ["Alice", 30, "São Paulo"],
        ["Bob", 24, "Rio de Janeiro"],
        ["Carlos", 35, "Belo Horizonte"],
        ["Diana", 28, "Porto Alegre"]
    ]

    with open(f"Atividade7/{filename}", 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    print(f"Arquivo '{filename}' criado com sucesso em Atividade7/.")

if __name__ == "__main__":
    create_personal_data_csv()
