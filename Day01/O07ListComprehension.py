
"""

comprehension is a way of iterating through a collection using lambda syntax

"""

squares = [x ** 2 for x in range(1, 11)]
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
words  = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
fruits = [
    ('apple', 285),
    ('orange', 80),
    ('grapes',120),
    ('banana', 65),
    ('gauva', 90),
    ('water melon', 75),
    ('strawberry', 350),
    ('mango', 180)
]
print(f"fruits :{fruits}")
print("-" * 60)

print(["fruit" for fruit in fruits])
print("-" * 60)

print([fruit for fruit in fruits])
print("-" * 60)

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")

print(f"prices :")
print("-" * 60)

print([price[1] * 0.9 for price in fruits])
print("-" * 60)

print([(price[1] * 0.9, price[1] * 0.75) for price  in fruits])

print("-" * 60)
print([(price[0], price[1], price[1] * 0.9, price[1] *.75) for price in fruits])

print("-" * 60)
print([(price[0], price[1], price[1] * 0.9, price[1] * 0.75) for price in fruits if price[1] > 100])

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(words)