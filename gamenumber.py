import random

print("=" * 40)
print("🎮 เกมทายตัวเลข (Guess the Number)")
print("=" * 40)

# สุ่มเลข 1-100
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("ทายตัวเลข (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("🔼 น้อยเกินไป")
    elif guess > secret_number:
        print("🔽 มากเกินไป")
    else:
        print(f"\n🎉 ถูกต้อง!")
        print(f"คุณใช้ทั้งหมด {attempts} ครั้ง")
        break

print("\nขอบคุณที่เล่นเกม 😊")