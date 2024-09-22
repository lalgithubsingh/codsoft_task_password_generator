import string
import random

def generate_password(length, use_special_chars=False):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of password: "))
        use_special_chars = input("Include special characters? y/n: ").lower() == 'y'
        if length <= 0:
            print("Password length should be a positive number.")
        else:
            password = generate_password(length, use_special_chars)
            print("Your Generated Password =", password)
    except ValueError:
        print("Invalid Input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()