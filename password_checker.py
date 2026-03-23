password = input("Please choose a password: ")

score = 0

feedback = []

if len(password) >= 8:
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

import string
if any(c in string.punctuation for c in password):
    score += 1

if score <= 2:
    strength = "Weak"
    
elif score <= 4:
    strength = "Medium"
    
else:
    strength = "Strong"

print(str(score) + ": " + strength)