import random
x = random.randint(1, 20)

print("O'yla izla top")

while True:
    y = int(input("Son kiriting: "))
    if y < x:
        print("Katta son.")
    elif y > x:
        print("Kichik son.")
    else:
        print(f"To'g'ri! Siz {x} sonini topdingiz.")
        break
