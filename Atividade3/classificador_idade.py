#!/usr/bin/env python3
def classificar_idade(idade):

    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

def main():
    """Função principal do programa"""
    print("Classificador de Idade")
    print("=" * 30)
    
    try:
        # Entrada: idade do usuário
        idade = int(input("Digite sua idade: "))
        
        # Validação da idade
        if idade < 0:
            print("Erro: A idade não pode ser negativa!")
            return
        
        # Classificação da idade
        categoria = classificar_idade(idade)
        
        # Saída da classificação
        print(f"\nSua idade é: {idade} anos")
        print(f"Categoria: {categoria}")
        
        # Exibição das faixas etárias para referência
        print("\nFaixas etárias:")
        print("• Criança: 0-12 anos")
        print("• Adolescente: 13-17 anos")
        print("• Adulto: 18-59 anos")
        print("• Idoso: 60 anos ou mais")
        
    except ValueError:
        print("Erro: Por favor, digite uma idade válida (número inteiro)!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
