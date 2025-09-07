x = "python123"
print("Parolni kiriting01:")
y = 0  

while y < 3:
    z = input("Parolni kiriting02: ")
    if z == x:
        print("Xush kelibsiz!")
        break
    else:
        y += 1
        if y < 3:
            print("Xato! Qayta urinib ko'ring.")
        else:
            print("Kirish bloklandi! Juda ko'p xato urinish.")
