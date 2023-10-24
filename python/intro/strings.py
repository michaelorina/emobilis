name = "Orinah"
city = "Cairo"
age = 22
weight = 70.8

print(name + city)
print(name * 4)
# print(name + age)

print(f"I am {name}, I am {age} years old and I live in {city}. I weigh {weight} Kgs")

sentence = "These are python functions to do with strings"

upper_case = sentence.upper()

print(upper_case)
print(sentence.upper())
print(upper_case.lower())
print(len(sentence))
print(sentence.capitalize())
print(name.swapcase())
print(sentence)
print(sentence.strip())

results = sentence.replace("functions", "methods").strip().upper()
print(results)