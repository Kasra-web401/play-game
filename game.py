import random

print("🎮 به بازی حدس عدد خوش آمدی!")
print("من یه عدد بین ۱ تا ۱۰۰ انتخاب کردم. تو باید حدس بزنی.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("حدس تو چیه؟ (یا بنویس 'خروج' برای بستن بازی): ")
    
    if guess == "خروج":
        print("بازی رو بستی. خداحافظ!")
        break
    
    try:
        guess = int(guess)
    except:
        print("لطفاً یه عدد صحیح وارد کن!")
        continue
    
    attempts += 1
    
    if guess < number:
        print("⬆️ عدد من بزرگتره!")
    elif guess > number:
        print("⬇️ عدد من کوچیکتره!")
    else:
        print(f"🎉 آفرین! درست حدس زدی! عدد {number} بود.")
        print(f"تو در {attempts} تلاش برنده شدی!")
        break