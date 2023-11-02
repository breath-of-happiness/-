money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0  # начальное число месяцев

while (spend - salary) < money_capital:
    month += 1
    money_capital = money_capital - (spend-salary)
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
