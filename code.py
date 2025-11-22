import random

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*']

upper_char = [c.upper() for c in char]  # Uppercase letters

all_char = char + upper_char + number + symbol  # Flat list

password = ''.join(random.sample(all_char, 8))
print(password)
