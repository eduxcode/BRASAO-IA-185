#!/usr/bin/env python3
def calcular_comissao(total_vendas):
  
    return total_vendas * 0.15

def calcular_total_receber(salario_fixo, comissao):
  
    return salario_fixo + comissao

def main():
    """Função principal do programa"""
    print("Calculadora de Comissão")
    print("=" * 30)
    print("Calcula o total a receber de um vendedor")
    print("(Salário fixo + 15% de comissão sobre vendas)")
    
    try:
        print("\n" + "="*50)
        
        # Entrada dos dados do vendedor
        nome = input("Digite o nome do vendedor: ").strip()
        
        # Validação do nome
        if not nome:
            print("Erro: O nome não pode estar vazio!")
            return
        
        # Entrada do salário fixo
        salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
        
        # Validação do salário
        if salario_fixo < 0:
            print("Erro: O salário fixo não pode ser negativo!")
            return
        
        # Entrada do total de vendas
        total_vendas = float(input("Digite o total de vendas efetuadas: R$ "))
        
        # Validação das vendas
        if total_vendas < 0:
            print("Erro: O total de vendas não pode ser negativo!")
            return
        
        # Cálculos
        comissao = calcular_comissao(total_vendas)
        total_receber = calcular_total_receber(salario_fixo, comissao)
        
        # Saída dos resultados
        print(f"\n{'='*60}")
        print("RELATÓRIO DE COMISSÃO")
        print(f"{'='*60}")
        print(f"Vendedor: {nome}")
        print(f"Salário Fixo: R$ {salario_fixo:.2f}")
        print(f"Total de Vendas: R$ {total_vendas:.2f}")
        print(f"Comissão (15%): R$ {comissao:.2f}")
        print(f"{'='*60}")
        print(f"TOTAL A RECEBER: R$ {total_receber:.2f}")
        print(f"{'='*60}")
        
        # Detalhamento dos cálculos
        print(f"\nDetalhamento:")
        print(f"• Salário fixo: R$ {salario_fixo:.2f}")
        print(f"• Comissão (15% de R$ {total_vendas:.2f}): R$ {comissao:.2f}")
        print(f"• Total: R$ {salario_fixo:.2f} + R$ {comissao:.2f} = R$ {total_receber:.2f}")
        
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos para salário e vendas!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
