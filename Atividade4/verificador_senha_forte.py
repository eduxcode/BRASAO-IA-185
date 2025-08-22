def verificar_comprimento(senha):
 
    return len(senha) >= 8

def verificar_numero(senha):
  
    return any(caractere.isdigit() for caractere in senha)

def verificar_maiuscula(senha):
  
    return any(caractere.isupper() for caractere in senha)

def verificar_minuscula(senha):
   
    return any(caractere.islower() for caractere in senha)

def verificar_caractere_especial(senha):
 
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(caractere in caracteres_especiais for caractere in senha)

def validar_senha(senha):
  
    resultados = {
        'comprimento': verificar_comprimento(senha),
        'numero': verificar_numero(senha),
        'maiuscula': verificar_maiuscula(senha),
        'minuscula': verificar_minuscula(senha),
        'especial': verificar_caractere_especial(senha)
    }
    
    # Critérios obrigatórios (mínimo)
    criterios_obrigatorios = ['comprimento', 'numero']
    senha_valida = all(resultados[criterio] for criterio in criterios_obrigatorios)
    
    # Critérios adicionais para senha muito forte
    criterios_adicionais = ['maiuscula', 'minuscula', 'especial']
    criterios_atingidos = sum(resultados[criterio] for criterio in criterios_adicionais)
    
    return {
        'valida': senha_valida,
        'resultados': resultados,
        'forca': calcular_forca_senha(senha_valida, criterios_atingidos),
        'pontuacao': criterios_atingidos
    }

def calcular_forca_senha(senha_valida, criterios_atingidos):
   
    if not senha_valida:
        return "❌ Muito Fraca (não atende aos critérios mínimos)"
    
    if criterios_atingidos == 0:
        return "🟡 Fraca (atende apenas aos critérios mínimos)"
    elif criterios_atingidos == 1:
        return "🟠 Média (atende a alguns critérios adicionais)"
    elif criterios_atingidos == 2:
        return "🟢 Forte (atende à maioria dos critérios)"
    else:
        return "🔒 Muito Forte (atende a todos os critérios)"

def exibir_resultado_validacao(senha, validacao):
    """
    Exibe o resultado detalhado da validação da senha.
    """
    print("\n" + "=" * 60)
    print("🔐 RESULTADO DA VALIDAÇÃO DA SENHA")
    print("=" * 60)
    
    # Força da senha
    print(f"💪 Força: {validacao['forca']}")
    
    # Critérios obrigatórios
    print("\n📋 CRITÉRIOS OBRIGATÓRIOS:")
    print(f"✅ Comprimento (≥8 caracteres): {'✅' if validacao['resultados']['comprimento'] else '❌'}")
    print(f"✅ Número: {'✅' if validacao['resultados']['numero'] else '❌'}")
    
    # Critérios adicionais
    print("\n📊 CRITÉRIOS ADICIONAIS:")
    print(f"✅ Letra maiúscula: {'✅' if validacao['resultados']['maiuscula'] else '❌'}")
    print(f"✅ Letra minúscula: {'✅' if validacao['resultados']['minuscula'] else '❌'}")
    print(f"✅ Caractere especial: {'✅' if validacao['resultados']['especial'] else '❌'}")
    
    # Pontuação
    print(f"\n🎯 Pontuação: {validacao['pontuacao']}/3 critérios adicionais")
    
    # Recomendações
    if not validacao['valida']:
        print("\n💡 RECOMENDAÇÕES:")
        if not validacao['resultados']['comprimento']:
            print("• Aumente o comprimento da senha para pelo menos 8 caracteres")
        if not validacao['resultados']['numero']:
            print("• Adicione pelo menos um número à senha")
    elif validacao['pontuacao'] < 3:
        print("\n💡 SUGESTÕES PARA FORTALECER:")
        if not validacao['resultados']['maiuscula']:
            print("• Adicione pelo menos uma letra maiúscula")
        if not validacao['resultados']['minuscula']:
            print("• Adicione pelo menos uma letra minúscula")
        if not validacao['resultados']['especial']:
            print("• Adicione pelo menos um caractere especial (!@#$%^&*)")
    
    print("=" * 60)

def obter_senha():
  
    while True:
        try:
            senha = input("\n🔐 Digite uma senha ou 'sair' para encerrar: ").strip()
            
            if senha.lower() == 'sair':
                return None
            
            if senha == "":
                print("❌ Erro: A senha não pode estar vazia!")
                continue
            
            return senha
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            exit()

def main():
    """
    Função principal do verificador de senhas.
    """
    print("🔐 VERIFICADOR DE SENHA FORTE")
    print("=" * 60)
    print("📋 CRITÉRIOS DE SENHA FORTE:")
    print("• ✅ Pelo menos 8 caracteres")
    print("• ✅ Pelo menos um número")
    print("• 💡 RECOMENDADO: Letras maiúsculas, minúsculas e caracteres especiais")
    print("=" * 60)
    
    contador_senhas = 0
    senhas_validas = 0
    
    while True:
        senha = obter_senha()
        
        if senha is None:  # Usuário digitou 'sair'
            break
        
        contador_senhas += 1
        print(f"\n🔍 Analisando senha #{contador_senhas}...")
        
        # Validar a senha
        validacao = validar_senha(senha)
        
        # Exibir resultado
        exibir_resultado_validacao(senha, validacao)
        
        # Contar senhas válidas
        if validacao['valida']:
            senhas_validas += 1
            print(f"\n🎉 Parabéns! Esta senha atende aos critérios mínimos de segurança!")
        
        # Perguntar se quer continuar
        if validacao['valida']:
            continuar = input("\n🔄 Deseja verificar outra senha? (s/n): ").strip().lower()
            if continuar not in ['s', 'sim', 'y', 'yes']:
                break
        else:
            print("\n🔄 Tente novamente com uma senha mais forte!")
    
    # Estatísticas finais
    print("\n" + "=" * 60)
    print("📊 ESTATÍSTICAS FINAIS")
    print("=" * 60)
    print(f"🔍 Total de senhas analisadas: {contador_senhas}")
    print(f"✅ Senhas válidas: {senhas_validas}")
    print(f"❌ Senhas inválidas: {contador_senhas - senhas_validas}")
    
    if contador_senhas > 0:
        taxa_sucesso = (senhas_validas / contador_senhas) * 100
        print(f"📈 Taxa de sucesso: {taxa_sucesso:.1f}%")
    
    print("\n👋 Programa encerrado. Obrigado por usar o verificador de senhas!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        print("O programa será encerrado.")
