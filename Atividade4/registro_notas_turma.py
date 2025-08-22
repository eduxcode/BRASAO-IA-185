def validar_nota(nota_str):
   
    try:
        nota = float(nota_str)
        return 0 <= nota <= 10
    except ValueError:
        return False

def obter_nota():
 
    while True:
        try:
            entrada = input("Digite uma nota (0-10) ou 'fim' para encerrar: ").strip().lower()
            
            if entrada == 'fim':
                return None
            
            if validar_nota(entrada):
                return float(entrada)
            else:
                print("❌ Nota inválida! Digite um número entre 0 e 10.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            exit()

def calcular_media(notas):
  
    if not notas:
        return 0
    return sum(notas) / len(notas)

def exibir_estatisticas(notas):
    """
    Exibe estatísticas detalhadas das notas da turma.
    """
    if not notas:
        print("📊 Nenhuma nota foi registrada.")
        return
    
    print("\n" + "=" * 50)
    print("📊 ESTATÍSTICAS DA TURMA")
    print("=" * 50)
    
    # Estatísticas básicas
    print(f"📝 Total de alunos: {len(notas)}")
    print(f"📊 Média da turma: {calcular_media(notas):.2f}")
    print(f"🔝 Maior nota: {max(notas):.1f}")
    print(f"🔻 Menor nota: {min(notas):.1f}")
    
    # Distribuição por faixas
    print("\n📈 DISTRIBUIÇÃO POR FAIXAS:")
    print("Excelente (9.0-10.0):", len([n for n in notas if n >= 9.0]))
    print("Muito Bom (8.0-8.9):", len([n for n in notas if 8.0 <= n < 9.0]))
    print("Bom (7.0-7.9):", len([n for n in notas if 7.0 <= n < 8.0]))
    print("Regular (6.0-6.9):", len([n for n in notas if 6.0 <= n < 7.0]))
    print("Insuficiente (0.0-5.9):", len([n for n in notas if n < 6.0]))
    
    print("=" * 50)

def main():
    """
    Função principal do programa de registro de notas.
    """
    print("🎓 SISTEMA DE REGISTRO DE NOTAS")
    print("=" * 50)
    print("📋 Instruções:")
    print("• Digite notas de 0 a 10")
    print("• Digite 'fim' para encerrar e ver as estatísticas")
    print("• Notas inválidas serão ignoradas")
    print("=" * 50)
    
    notas = []
    contador_notas = 0
    contador_invalidas = 0
    
    while True:
        nota = obter_nota()
        
        if nota is None:  # Usuário digitou 'fim'
            break
        
        notas.append(nota)
        contador_notas += 1
        
        print(f"✅ Nota {contador_notas}: {nota:.1f} registrada com sucesso!")
        
        # Mostrar estatísticas parciais a cada 5 notas
        if contador_notas % 5 == 0:
            print(f"\n📊 Estatísticas parciais: {contador_notas} notas registradas")
            print(f"📈 Média atual: {calcular_media(notas):.2f}")
            print("-" * 30)
    
    # Exibir estatísticas finais
    if notas:
        print(f"\n🎯 REGISTRO FINALIZADO!")
        print(f"📝 Total de notas válidas registradas: {contador_notas}")
        print(f"❌ Notas inválidas ignoradas: {contador_invalidas}")
        
        exibir_estatisticas(notas)
        
        # Perguntar se quer ver as notas individuais
        ver_notas = input("\n👀 Deseja ver todas as notas registradas? (s/n): ").strip().lower()
        if ver_notas in ['s', 'sim', 'y', 'yes']:
            print("\n📋 NOTAS REGISTRADAS:")
            for i, nota in enumerate(notas, 1):
                print(f"Aluno {i:2d}: {nota:5.1f}")
    else:
        print("\n❌ Nenhuma nota foi registrada.")
    
    print("\n👋 Programa encerrado. Obrigado por usar o sistema!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        print("O programa será encerrado.")
