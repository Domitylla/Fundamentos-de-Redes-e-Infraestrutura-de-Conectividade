# revisao_1_ex30.py
idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 10:
    print("Infantil B")
elif 11 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Sênior")
else:
    print("Sem categoria")
