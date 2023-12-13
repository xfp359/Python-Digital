def required_money_capital(salary, spend, increase, months_to_survive):
    money_capital = 0  # Изначально подушка безопасности равна нулю
    remaining_months = months_to_survive

    while remaining_months > 0:
        budget_this_month = salary + money_capital
        if spend > budget_this_month:
            money_capital += spend - budget_this_month
            spend *= (1 + increase / 100)
            remaining_months -= 1
        else:
            break

    return round(money_capital, 2)

salary = 50000  # Ежемесячная зарплата в рублях
spend = 55000  # Расходы на проживание в рублях
increase = 3  # Ежемесячный рост цен в процентах
months_to_survive = 10  # Сколько месяцев протянуть без долгов

result = required_money_capital(salary, spend, increase, months_to_survive)
print(f"Необходимая подушка безопасности: {result} руб.")
