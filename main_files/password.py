import random
import string

def generate_password(n):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    possible_characters = letters + digits + punctuation

    random_chars = random.choices(possible_characters, k=n)

    password = "".join(random_chars)
    return password


password = generate_password(12)
print(f"Your password is: {password}")

