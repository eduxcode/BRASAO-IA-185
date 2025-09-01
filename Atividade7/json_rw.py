import json
import sys

def write_json_data(filename="personal_data.json"):
    person_data = {
        "nome": "Fernanda",
        "idade": 29,
        "cidade": "Curitiba"
    }

    with open(f"Atividade7/{filename}", 'w', encoding='utf-8') as jsonfile:
        json.dump(person_data, jsonfile, ensure_ascii=False, indent=4)
    print(f"Dados escritos em '{filename}' com sucesso em Atividade7/.")
    sys.stdout.flush()

def read_json_data(filename="personal_data.json"):
    try:
        with open(f"Atividade7/{filename}", 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            print(f"\nDados lidos de '{filename}':")
            print(json.dumps(data, ensure_ascii=False, indent=4))
            sys.stdout.flush()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado em Atividade7/.")
        sys.stdout.flush()
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o JSON do arquivo '{filename}'.")
        sys.stdout.flush()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.stdout.flush()

if __name__ == "__main__":
    write_json_data()
    read_json_data()
