def obter_numero(mensagem):
  
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("❌ Erro: Entrada inválida! Digite um número válido.")
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            exit()

def obter_operacao():
  
    operacoes_validas = ['+', '-', '*', '/']
    
    while True:
        try:
            operacao = input("Digite a operação (+, -, *, /): ").strip()
            
            if operacao in operacoes_validas:
                return operacao
            else:
                print("❌ Erro: Operação inválida! Use apenas: +, -, *, /")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            exit()

def realizar_calculo(num1, num2, operacao):
  
    try:
        if operacao == '+':
            resultado = num1 + num2
            return resultado
        elif operacao == '-':
            resultado = num1 - num2
            return resultado
        elif operacao == '*':
            resultado = num1 * num2
            return resultado
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida!")
            resultado = num1 / num2
            return resultado
    except ZeroDivisionError as e:
        raise e

def main():
    """
    Função principal da calculadora.
    """
    print("🧮 CALCULADORA BÁSICA")
    print("=" * 30)
    print("Operações disponíveis: +, -, *, /")
    print("=" * 30)
    
    while True:
        try:
            # Obter os números
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            # Obter a operação
            operacao = obter_operacao()
            
            # Realizar o cálculo
            resultado = realizar_calculo(num1, num2, operacao)
            
            # Exibir o resultado
            print("\n" + "=" * 30)
            print(f"📊 RESULTADO:")
            print(f"{num1} {operacao} {num2} = {resultado}")
            print("=" * 30)
            
            # Verificar se o usuário quer continuar
            continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                print("\n👋 Obrigado por usar a calculadora! Até logo!")
                break
            else:
                print("\n" + "=" * 30 + "\n")
                
        except ZeroDivisionError as e:
            print(f"❌ Erro: {e}")
            print("🔄 Tente novamente com números diferentes.\n")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("🔄 Tente novamente.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        print("O programa será encerrado.")
