#!/usr/bin/env python3
import math

def calcular_area_circunferencia(raio):

    pi = 3.14159265
    area = pi * (raio ** 2)
    return area

def main():
    """Função principal do programa"""
    print("Calculadora de Área da Circunferência")
    print("=" * 40)
    
    try:
        # Entrada: valor do raio
        raio = float(input("Digite o valor do raio: "))
        
        # Validação do raio
        if raio <= 0:
            print("Erro: O raio deve ser um valor positivo!")
            return
        
        # Cálculo da área
        area = calcular_area_circunferencia(raio)
        
        # Saída formatada com 4 casas decimais
        print(f"A={area:.4f}")
        
    except ValueError:
        print("Erro: Por favor, digite um número válido!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
