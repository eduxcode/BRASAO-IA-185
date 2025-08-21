#!/usr/bin/env python3

def calcular_media_ponderada(n1, n2, n3, n4):
    """Calcula a média ponderada com pesos 2, 3, 4 e 1."""
    pesos = 2 + 3 + 4 + 1
    soma_ponderada = (n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)
    return soma_ponderada / pesos

def main():
    """Função principal do programa"""
    try:
        # Entrada das quatro notas
        n1 = float(input("Digite N1 (com uma casa decimal): "))
        n2 = float(input("Digite N2 (com uma casa decimal): "))
        n3 = float(input("Digite N3 (com uma casa decimal): "))
        n4 = float(input("Digite N4 (com uma casa decimal): "))

        media = calcular_media_ponderada(n1, n2, n3, n4)
        print(f"Media: {media:.1f}")

        if media >= 7.0:
            print("Aluno aprovado.")
        elif media < 5.0:
            print("Aluno reprovado.")
        else:
            # Aluno em exame
            print("Aluno em exame.")
            exame = float(input("Digite a nota do exame: "))
            print(f"Nota do exame: {exame:.1f}")
            media_final = (media + exame) / 2
            if media_final >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print(f"Media final: {media_final:.1f}")

    except ValueError:
        print("Erro: Por favor, digite números válidos com uma casa decimal.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
