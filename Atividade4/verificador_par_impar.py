def verificar_par_impar(numero):
 
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def validar_numero_inteiro(entrada):
  
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        return None

def obter_numero():
   
    while True:
        try:
            entrada = input("\n🔢 Digite um número inteiro ou 'fim' para encerrar: ").strip()
            
            if entrada.lower() == 'fim':
                return None, 'fim'
            
            if entrada == "":
                print("❌ Erro: A entrada não pode estar vazia!")
                continue
            
            numero = validar_numero_inteiro(entrada)
            if numero is not None:
                return numero, 'valido'
            else:
                print("❌ Erro: Digite apenas números inteiros!")
                return None, 'invalido'
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            exit()

def exibir_resultado_numero(numero, tipo, contador):
    """
    Exibe o resultado da verificação de um número específico.
    """
    print(f"✅ Número {contador}: {numero} é {tipo.upper()}!")

def exibir_estatisticas_parciais(contador_pares, contador_impares, total):
    """
    Exibe estatísticas parciais a cada 10 números válidos.
    """
    print(f"\n📊 Estatísticas parciais ({total} números analisados):")
    print(f"   🟢 Pares: {contador_pares}")
    print(f"   🔵 Ímpares: {contador_impares}")
    print("-" * 40)

def exibir_estatisticas_finais(contador_pares, contador_impares, contador_validos, contador_invalidos):
    """
    Exibe as estatísticas finais do programa.
    """
    total_entradas = contador_validos + contador_invalidos
    
    print("\n" + "=" * 60)
    print("📊 ESTATÍSTICAS FINAIS")
    print("=" * 60)
    
    # Números válidos analisados
    print(f"🔢 Total de números válidos analisados: {contador_validos}")
    print(f"🟢 Números pares: {contador_pares}")
    print(f"🔵 Números ímpares: {contador_impares}")
    
    # Percentuais se houver números válidos
    if contador_validos > 0:
        percentual_pares = (contador_pares / contador_validos) * 100
        percentual_impares = (contador_impares / contador_validos) * 100
        print(f"📈 Percentual de pares: {percentual_pares:.1f}%")
        print(f"📈 Percentual de ímpares: {percentual_impares:.1f}%")
    
    # Entradas inválidas
    if contador_invalidos > 0:
        print(f"\n❌ Entradas inválidas: {contador_invalidos}")
        print(f"📊 Total de tentativas: {total_entradas}")
        taxa_sucesso = (contador_validos / total_entradas) * 100
        print(f"✅ Taxa de sucesso: {taxa_sucesso:.1f}%")
    
    # Resumo por categoria
    print(f"\n📋 RESUMO:")
    if contador_pares > contador_impares:
        print(f"🏆 Mais números pares foram inseridos ({contador_pares} vs {contador_impares})")
    elif contador_impares > contador_pares:
        print(f"🏆 Mais números ímpares foram inseridos ({contador_impares} vs {contador_pares})")
    else:
        print(f"⚖️ Empate! Mesma quantidade de pares e ímpares ({contador_pares} cada)")
    
    print("=" * 60)

def main():
    """
    Função principal do verificador de números pares e ímpares.
    """
    print("🔢 VERIFICADOR DE NÚMEROS PARES E ÍMPARES")
    print("=" * 60)
    print("📋 Instruções:")
    print("• Digite números inteiros para verificar se são pares ou ímpares")
    print("• Digite 'fim' para encerrar e ver as estatísticas")
    print("• Entradas inválidas serão rejeitadas com mensagem de erro")
    print("=" * 60)
    
    contador_pares = 0
    contador_impares = 0
    contador_validos = 0
    contador_invalidos = 0
    
    while True:
        numero, status = obter_numero()
        
        if status == 'fim':
            break
        elif status == 'invalido':
            contador_invalidos += 1
            continue
        elif status == 'valido':
            contador_validos += 1
            
            # Verificar se é par ou ímpar
            tipo = verificar_par_impar(numero)
            
            # Contar pares e ímpares
            if tipo == 'par':
                contador_pares += 1
            else:
                contador_impares += 1
            
            # Exibir resultado
            exibir_resultado_numero(numero, tipo, contador_validos)
            
            # Mostrar estatísticas parciais a cada 10 números válidos
            if contador_validos % 10 == 0:
                exibir_estatisticas_parciais(contador_pares, contador_impares, contador_validos)
    
    # Exibir estatísticas finais
    if contador_validos > 0 or contador_invalidos > 0:
        print(f"\n🎯 ANÁLISE FINALIZADA!")
        print(f"📝 Total de números válidos processados: {contador_validos}")
        if contador_invalidos > 0:
            print(f"❌ Entradas inválidas rejeitadas: {contador_invalidos}")
        
        exibir_estatisticas_finais(contador_pares, contador_impares, contador_validos, contador_invalidos)
        
        # Perguntar se quer ver detalhes adicionais
        if contador_validos >= 5:
            ver_detalhes = input("\n👀 Deseja ver análise detalhada? (s/n): ").strip().lower()
            if ver_detalhes in ['s', 'sim', 'y', 'yes']:
                print("\n🔍 ANÁLISE DETALHADA:")
                print(f"• Maior tendência: {'Números pares' if contador_pares > contador_impares else 'Números ímpares' if contador_impares > contador_pares else 'Equilíbrio entre pares e ímpares'}")
                print(f"• Eficiência de entrada: {((contador_validos / (contador_validos + contador_invalidos)) * 100):.1f}% das entradas foram válidas" if contador_invalidos > 0 else "100% das entradas foram válidas")
    else:
        print("\n❌ Nenhum número foi processado.")
    
    print("\n👋 Programa encerrado. Obrigado por usar o verificador!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        print("O programa será encerrado.")
