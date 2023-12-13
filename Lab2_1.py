def months_to_run_out_of_money(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= 0:
        budget_this_month = salary + money_capital
        if spend > budget_this_month:
            break

        money_capital -= spend
        spend *= (1 + increase / 100)
        months += 1

    return months

money_capital = 100000  # Финансовая подушка безопасности в рублях
salary = 50000  # Ежемесячная зарплата в рублях
spend = 60000  # Расходы на проживание в рублях
increase = 5  # Ежемесячный рост цен в процентах

result = months_to_run_out_of_money(money_capital, salary, spend, increase)
print(f"Можно протянуть без долгов {result} месяца/месяцев.")
