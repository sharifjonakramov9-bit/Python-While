print("| Mini kalkulyator! |")

while True:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))

    x = input("Amalni tanlang: ")

    if x == "+":
        res = a + b
    elif x == "-":
        res = a - b
    elif x == "*":
        res = a * b
    elif x == "/":
        if b != 0:
            res = a / b
        else:
            res = " Nolga bo'lish mumkin emas!"
    else:
        res = "Noto'g'ri amal tanlandi!"
    print(f"Natija: {res}")
    z = input("Davom etasizmi? (ha/yo'q): ")
    if z.lower() != "ha":
        print("Dastur tugadi.")
        break
# buni chatGPTdan so'rab so'rab qildim oson bo'lmadi
