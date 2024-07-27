import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
arr = np.sqrt(arr)
print(arr)
arr = np.sin(arr)
print(arr)
arr = np.cos(arr)
print(arr)
arr = np.log(arr)
print(arr)
arr = np.exp(arr)
print(arr)

print("\n\n\n")

# Данные о рекламных кампаниях
campaign_costs = np.array([200, 300, 150, 400, 250])
clicks = np.array([1000, 1500, 1200, 800, 2000])
# Расчет стоимости клика
cost_per_click = campaign_costs / clicks
# Вывод результатов
print("Стоимость клика для каждой кампании:", cost_per_click)


print("\n\n\n")

# Данные о продажах за неделю
weekly_sales = np.array([500, 600, 800, 700, 900, 1000, 1200])
# Вычисление общей суммы продаж
total_sales = np.sum(weekly_sales)
# Вычисление средней цены продажи
average_price = np.mean(weekly_sales)
# Вывод результатов
print("Общая сумма продаж за неделю:", total_sales)
print("Средняя цена продажи:", average_price)