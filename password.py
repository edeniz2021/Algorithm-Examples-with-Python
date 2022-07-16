import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
a  = int(input("Kac harften olussun :"))
b  = int(input("Kac sembol olsun : "))
c = int(input("kac rakam olsun : "))
pas = []
for i in range(0,b):
    pas +=random.choice(symbols)
for i in range(0,c):
    pas += random.choice(numbers)
for i in range(0,a-b-c):
    pas += random.choice(letters)
random.shuffle(pas)
print(f"Your password is: {pas}")