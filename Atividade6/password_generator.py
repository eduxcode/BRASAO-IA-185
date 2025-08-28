
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Informe a quantidade de caracteres para a senha: "))
            if password_length <= 0:
                print("Por favor, insira um número positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    random_password = generate_random_password(password_length)
    print("Senha aleatória gerada:", random_password)
