
l1 = list(range(1, 26))
print(f"l1 :{l1}")

even_nums = list(filter(lambda x: x % 2 == 0, l1))
print(f"Even Numbers :{even_nums}")
print("-" * 60)

odd_nums = list(filter(lambda x: x % 2 == 1, l1))
print(f"Odd Numbers :{odd_nums}")

print("-" * 60)
sentence = 'the quick brown fox jumps over the lazy dog'
print(f"sentence :{sentence}")

print("-" * 60)
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")
