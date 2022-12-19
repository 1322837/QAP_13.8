quant = int(input("Введите количество билетов которые вы собираетесь купить: "))
age = [int(input(f"Введите возраст получателя билета № {i+1}: ", )) for i in range(quant)]
pay = int()
for j in range(0, quant):
    if age[j] >= 25:
        pay = pay + 1390
    elif 18 <= age[j] <= 25:
        pay = pay + 990
    else:
        pay = pay
if quant > 3:
    pay = pay*0.9
pay_rounded = round(pay)
print("К оплате:", pay_rounded)