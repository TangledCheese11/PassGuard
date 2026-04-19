import sys

# Disable colours in IDLE
supports_color = sys.stdout.isatty() and "idlelib" not in sys.modules

def color(text, code):
    return f"{code}{text}\033[0m" if supports_color else text

ORANGE = "\033[38;5;208m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


password = input("Enter your password: ")
password_len = len(password)
numb = False
score = 0
# Check if the password has at least 1 digit
for char in password:
    if char.isdigit():
        numb = True
        score = score + 15
        break
if numb == False:
        print("Add a digit")

# Check is the password has one uppercase letter
up = False
for char in password:
     if char.isupper():
        up = True
        score = score + 15
        break
if up == False:
        print("Add an uppercase letter")

# Check if the password has one lowercase letter
lower = False
for char in password:
     if char.islower():
          lower = True
          score = score + 15
          break
if lower == False:
     print("Add a lowercase letter")

# Check if password has one special symbol
special = False
for char in password:
     if not char.isalnum():
          special = True
          score = score + 15
          break
if special == False:
     print("Add a special symbol")

# Testing Password Length
length_score = min(password_len * 4,40)


#Bar of strength
total = length_score + score
filled = total // 10
empty = 10 - filled
bar = "▰" * filled + "▱" * empty



# Return password strength
if total <= 30:
    print(color(f"CRITICAL WARNING! Your password integrity is very weak at {total}%", RED))
    print(color(f"[{bar}] {total}%", RED))

elif total <= 60:
    print(color(f"It is recommended to change your password! Current strength at {total}%", ORANGE))
    print(color(f"[{bar}] {total}%", ORANGE))

elif total <= 80:
    print(color(f"Moderate level password, Strength at {total}%", YELLOW))
    print(color(f"[{bar}] {total}%", YELLOW))

else:
    print(color(f"Optimal password! High security {total}%", GREEN))
    print(color(f"[{bar}] {total}%", GREEN))
