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

#Set colors of strength
RED     = "\033[31m"
ORANGE  = "\033[38;5;208m"  
YELLOW  = "\033[33m"
GREEN   = "\033[32m"
RESET   = "\033[0m"

#Bar of strength
total = length_score + score
filled = total // 10
empty = 10 - filled
bar = "▰" * filled + "▱" * empty



# Return password strength
if total <= 30:
     print(RED,"CRITICAL WARNING! Your password integrity is very weak at",total,"%",RESET)
     print(RED + f"[{bar}] {total}%" + RESET)

elif total <= 60:
     print(ORANGE,"It is reccomended to change your password! Current strength at",total,"%",RESET)
     print(ORANGE + f"[{bar}] {total}%" + RESET)

elif total <= 80:
     print(YELLOW,"Moderate level password, Strength at ",total,"%",RESET)
     print(YELLOW + f"[{bar}] {total}%" + RESET)

else:
      if total <= 100:
        print(GREEN,"Optimal password! High security",total,"%",RESET)
        print(GREEN + f"[{bar}] {total}%" + RESET)