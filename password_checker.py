import string

password = input("Please choose a password: ")

score = 0

feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Password must be 8 characters or more")

if any(c.islower() for c in password):
    score += 1
else:
    feedback.append("Try adding some lowercase characters")

if any(c.isupper() for c in password):
    score += 1
else:
    feedback.append("Try adding some uppercase characters")

if any(c.isdigit() for c in password):
    score += 1
else:
    feedback.append("Try adding some numbers")


if any(c in string.punctuation for c in password):
    score += 1
else:
    feedback.append("Try adding some special characters (?, @, !, etc.)")

if score <= 2:
    strength = "Weak"
    
elif score <= 4:
    strength = "Medium"
    
else:
    strength = "Strong"

print(str(score) + ": " + strength)
for tip in feedback:
    print("-", tip)