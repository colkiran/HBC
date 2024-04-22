
res = {x: y for x in range(1, 6) for y in range(5, 11)}
print(f"res :{res}")
print("-" * 60)

sentence = "the quick brown fox jumps over the lazy dog"
words = {word: len(word) for word in sentence.split()}
print(f"words :{words}")

players = {
    'sachin' : (201, 245, 200, 265, 300),
    'sourav' : (180, 225, 200, 250, 383),
    'sehwag' : (230, 350, 285, 400, 350),
    'rahul' : (185, 245, 150, 225, 175),
    'laxman' : (201, 190, 145, 265, 182),
    'yuvraj' : (190, 120, 220, 165, 205)
}

print(f"players :{players}")
print(type(players))

print("-" * 60)
print(f"sachin :{players['sachin']}")

print("-" * 60)
print(f"sachin :{sum(players['sachin'])}")

print("-" * 60)
print({k: sum(v) for k, v in players.items()})

print("-" * 60)
print({k: sum(v) / len(v) for k, v in players.items()})

print("-" * 60)
print([x for x in players.values()])

print("-" * 60)
print([x for runs in players.values() for x in runs])

print("-" * 60)
print([x for runs in players.values() for x in runs if x >= 200])

print("-" * 60)
print({name: [scr for scr in score if scr >= 200] for name, score in players.items()})






