from datetime import date

def calculate_age_in_days(birth_year: int, birth_month: int = 1, birth_day: int = 1) -> int:
    """
    Calcula a idade de uma pessoa em dias, baseada na data de nascimento.

    Parâmetros:
        birth_year (int): O ano de nascimento (ex: 1990).
        birth_month (int): O mês de nascimento (padrão: 1 - Janeiro).
        birth_day (int): O dia de nascimento (padrão: 1 - Primeiro dia do mês).

    Retorna:
        int: A idade da pessoa em dias.
    """
    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    age_in_days = (today - birth_date).days
    return age_in_days

if __name__ == "__main__":
    # Exemplo de uso
    ano_nascimento = 1990
    mes_nascimento = 5
    dia_nascimento = 15
    idade_dias = calculate_age_in_days(ano_nascimento, mes_nascimento, dia_nascimento)
    print(f"Uma pessoa nascida em {dia_nascimento}/{mes_nascimento}/{ano_nascimento} tem {idade_dias} dias de vida.")

    ano_nascimento_2 = 2000
    idade_dias_2 = calculate_age_in_days(ano_nascimento_2)
    print(f"Uma pessoa nascida em 01/01/{ano_nascimento_2} tem {idade_dias_2} dias de vida.")
