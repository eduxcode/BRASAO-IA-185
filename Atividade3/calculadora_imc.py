#!/usr/bin/env python3
def calcular_imc(peso, altura):
 
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    """Função principal do programa"""
    print("Calculadora de IMC (Índice de Massa Corporal)")
    print("=" * 50)
    
    try:
        # Entrada: peso e altura do usuário
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        # Validação dos dados de entrada
        if peso <= 0:
            print("Erro: O peso deve ser um valor positivo!")
            return
        
        if altura <= 0:
            print("Erro: A altura deve ser um valor positivo!")
            return
        
        if altura > 3:  # Verificação para altura em metros (não em cm)
            print("Atenção: Certifique-se de que a altura está em metros (ex: 1.75)")
            confirmacao = input("Deseja continuar mesmo assim? (s/n): ").lower()
            if confirmacao != 's':
                return
        
        # Cálculo do IMC
        imc = calcular_imc(peso, altura)
        
        # Classificação do IMC
        classificacao = classificar_imc(imc)
        
        # Saída dos resultados
        print(f"\n{'='*50}")
        print("RESULTADOS:")
        print(f"{'='*50}")
        print(f"Peso: {peso:.1f} kg")
        print(f"Altura: {altura:.2f} m")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print(f"{'='*50}")
        
        # Exibição da tabela de referência
        print("\nTABELA DE REFERÊNCIA IMC:")
        print("• Abaixo do peso: IMC < 18.5")
        print("• Peso normal: IMC 18.5 - 24.9")
        print("• Sobrepeso: IMC 25.0 - 29.9")
        print("• Obeso: IMC ≥ 30.0")
        
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
