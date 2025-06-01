import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔒 Генератор случайных паролей 🔒")
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        if length < 4:
            print("Пароль должен быть не короче 4 символов!")
        else:
            password = generate_password(length)
            print(f"🔑 Ваш пароль: {password}")
    except ValueError:
        print("Ошибка: введите число!")
