import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

list_length = len(names) - 1
rouletted = random.randint(0, list_length)
print(names[rouletted])