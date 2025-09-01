import csv

def read_personal_data_csv(filename="personal_data.csv"):
    try:
        with open(f"Atividade7/{filename}", 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print(", ".join(row))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado em Atividade7/.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    read_personal_data_csv()
