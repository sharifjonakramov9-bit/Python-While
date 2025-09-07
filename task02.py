#Biror **maxfiy parol** oldindan belgilanadi, masalan `"python123"`.
#* Foydalanuvchi **while loop** orqali parol kiritadi.
#* To‘g‘ri bo‘lmasa: `"Xato! Qayta urinib ko‘ring."` chiqadi.
#* To‘g‘ri kiritganda: `"Xush kelibsiz!"` chiqadi va loop tugaydi.
x = "python123"
print("Parolni kiriting:")

while True:
    y = input("Parolni kiriting: ")
    if y == x:
        print("Xush kelibsiz!")
        break
    else:
        print("Xato! Qayta urinib ko'ring.")
