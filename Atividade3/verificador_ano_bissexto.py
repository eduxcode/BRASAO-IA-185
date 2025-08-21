#!/usr/bin/env python3

def verificar_ano_bissexto(ano):

    # Um ano é bissexto se:
    # - É divisível por 4 E
    # - NÃO é divisível por 100 OU é divisível por 400
    if ano % 4 == 0:
        if ano % 100 == 0:
            # Ano centenário: deve ser divisível por 400
            return ano % 400 == 0
        else:
            # Ano divisível por 4 mas não centenário
            return True
    else:
        # Não é divisível por 4
        return False

def explicar_regra_bissexto(ano):
 
    if ano % 4 != 0:
        return f"{ano} NÃO é bissexto porque não é divisível por 4"
    
    if ano % 100 == 0:
        if ano % 400 == 0:
            return f"{ano} É bissexto porque é divisível por 400 (regra especial para anos centenários)"
        else:
            return f"{ano} NÃO é bissexto porque é divisível por 100 mas não por 400"
    else:
        return f"{ano} É bissexto porque é divisível por 4"

def main():
    """Função principal do programa"""
    print("Verificador de Ano Bissexto")
    print("=" * 35)
    print("Determina se um ano é bissexto ou não")
    print("\nRegras para ano bissexto:")
    print("• Deve ser divisível por 4")
    print("• Se for divisível por 100, deve ser divisível por 400 também")
    
    while True:
        try:
            print("\n" + "="*50)
            
            # Entrada do ano
            ano = int(input("Digite um ano (ou 0 para sair): "))
            
            # Verificação para sair
            if ano == 0:
                print("\nObrigado por usar o Verificador de Ano Bissexto!")
                break
            
            # Validação do ano
            if ano < 0:
                print("Erro: O ano deve ser um valor positivo!")
                continue
            
            # Verificação se é bissexto
            eh_bissexto = verificar_ano_bissexto(ano)
            
            # Explicação da regra aplicada
            explicacao = explicar_regra_bissexto(ano)
            
            # Saída do resultado
            print(f"\n{'='*50}")
            print("RESULTADO:")
            print(f"{'='*50}")
            
            if eh_bissexto:
                print(f"✅ {ano} É um ano bissexto!")
            else:
                print(f"❌ {ano} NÃO é um ano bissexto!")
            
            print(f"\nExplicação:")
            print(f"{explicacao}")
            
            # Informações adicionais
            print(f"\nDetalhes técnicos:")
            print(f"• {ano} ÷ 4 = {ano/4:.2f} (resto: {ano % 4})")
            if ano % 100 == 0:
                print(f"• {ano} ÷ 100 = {ano/100:.2f} (resto: {ano % 100})")
                print(f"• {ano} ÷ 400 = {ano/400:.2f} (resto: {ano % 400})")
            print(f"{'='*50}")
            
            # Pergunta se deseja continuar
            continuar = input("\nDeseja verificar outro ano? (s/n): ").lower()
            if continuar != 's':
                print("\nObrigado por usar o Verificador de Ano Bissexto!")
                break
                
        except ValueError:
            print("Erro: Por favor, digite um ano válido (número inteiro)!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
