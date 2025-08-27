import re

def is_palindrome(text: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo.

    Parâmetros:
        text (str): A palavra ou frase a ser verificada.

    Retorna:
        bool: True se for um palíndromo, False caso contrário.
    """
    # Remove espaços, pontuação e converte para minúsculas
    processed_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return processed_text == processed_text[::-1]

if __name__ == "__main__":
    # Exemplos de uso
    frase1 = "A man, a plan, a canal: Panama"
    print(f"'{frase1}' é um palíndromo? {'Sim' if is_palindrome(frase1) else 'Não'}")

    frase2 = "racecar"
    print(f"'{frase2}' é um palíndromo? {'Sim' if is_palindrome(frase2) else 'Não'}")

    frase3 = "hello"
    print(f"'{frase3}' é um palíndromo? {'Sim' if is_palindrome(frase3) else 'Não'}")

    frase4 = "Madam"
    print(f"'{frase4}' é um palíndromo? {'Sim' if is_palindrome(frase4) else 'Não'}")

    frase5 = "No lemon, no melon"
    print(f"'{frase5}' é um palíndromo? {'Sim' if is_palindrome(frase5) else 'Não'}")
