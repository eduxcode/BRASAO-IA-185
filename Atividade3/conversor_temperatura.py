#!/usr/bin/env python3
def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin"""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin"""
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius"""
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit"""
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def converter_temperatura(temperatura, unidade_origem, unidade_destino):

    # Normaliza as unidades para maiúsculas
    origem = unidade_origem.upper()
    destino = unidade_destino.upper()
    
    # Se origem e destino são iguais, retorna o mesmo valor
    if origem == destino:
        return temperatura
    
    # Conversões a partir de Celsius
    if origem == 'C':
        if destino == 'F':
            return celsius_para_fahrenheit(temperatura)
        elif destino == 'K':
            return celsius_para_kelvin(temperatura)
    
    # Conversões a partir de Fahrenheit
    elif origem == 'F':
        if destino == 'C':
            return fahrenheit_para_celsius(temperatura)
        elif destino == 'K':
            return fahrenheit_para_kelvin(temperatura)
    
    # Conversões a partir de Kelvin
    elif origem == 'K':
        if destino == 'C':
            return kelvin_para_celsius(temperatura)
        elif destino == 'F':
            return kelvin_para_fahrenheit(temperatura)
    
    # Se chegou aqui, as unidades são inválidas
    raise ValueError(f"Conversão de {origem} para {destino} não é suportada")

def exibir_unidades():
    """Exibe as unidades disponíveis"""
    print("\nUnidades disponíveis:")
    print("• C - Celsius")
    print("• F - Fahrenheit") 
    print("• K - Kelvin")

def main():
    """Função principal do programa"""
    print("Conversor de Temperatura")
    print("=" * 30)
    print("Converte entre Celsius, Fahrenheit e Kelvin")
    
    while True:
        try:
            print("\n" + "="*50)
            
            # Entrada da temperatura
            temperatura = float(input("Digite a temperatura: "))
            
            # Entrada da unidade de origem
            exibir_unidades()
            unidade_origem = input("Digite a unidade de origem (C/F/K): ").strip()
            
            # Entrada da unidade de destino
            unidade_destino = input("Digite a unidade de destino (C/F/K): ").strip()
            
            # Validação das unidades
            unidades_validas = ['C', 'F', 'K']
            if unidade_origem.upper() not in unidades_validas:
                print("Erro: Unidade de origem inválida!")
                continue
                
            if unidade_destino.upper() not in unidades_validas:
                print("Erro: Unidade de destino inválida!")
                continue
            
            # Conversão da temperatura
            resultado = converter_temperatura(temperatura, unidade_origem, unidade_destino)
            
            # Saída do resultado
            print(f"\n{'='*50}")
            print("RESULTADO DA CONVERSÃO:")
            print(f"{'='*50}")
            print(f"{temperatura}°{unidade_origem.upper()} = {resultado:.2f}°{unidade_destino.upper()}")
            print(f"{'='*50}")
            
            # Pergunta se deseja continuar
            continuar = input("\nDeseja fazer outra conversão? (s/n): ").lower()
            if continuar != 's':
                print("\nObrigado por usar o Conversor de Temperatura!")
                break
                
        except ValueError as e:
            if "Conversão" in str(e):
                print(f"Erro: {e}")
            else:
                print("Erro: Por favor, digite um valor numérico válido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
