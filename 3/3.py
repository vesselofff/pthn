users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan',  'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

print("sperva vvoditsya tip sortirovki:")
print("1. Po vozrastu")
print("2. Po pervoi bukve logina")
print("3. Po gruppe")

try:
    sort_type = int(input("Tip sortirovki: "))
except ValueError:
    print("Oshibka: vvedite chislo 1, 2 ili 3.")
    exit()

if sort_type not in (1, 2, 3):
    print("Oshibka: nevernyi tip sortirovki.")
    exit()

criteria = input("Vvedite kriterii poiska: ").strip()

filtered = []

if sort_type == 1:
    try:
        min_age = int(criteria)
    except ValueError:
        print("Oshibka: vozrast dolzhen byt chislom.")
        exit()
    filtered = [u for u in users if u['age'] > min_age]
    filtered.sort(key=lambda x: x['age'])

elif sort_type == 2:
    target_letter = criteria.upper()
    filtered = [u for u in users if u['login'].upper().startswith(target_letter)]
    filtered.sort(key=lambda x: x['login'])

elif sort_type == 3:
    target_group = criteria
    filtered = [u for u in users if u['group'] == target_group]
    filtered.sort(key=lambda x: (x['group'], x['login']))

if not filtered:
    print("Net polzovatelei, podhodyashchih pod kriterii.")
else:
    for user in filtered:
        age = user['age']
        if age % 100 in (11, 12, 13, 14):
            suffix = "let"
        elif age % 10 == 1:
            suffix = "god"
        else:
            suffix = "goda"
        print(f"Polzovatel: '{user['login']}' vozrast {age} {suffix}, gruppa \"{user['group']}\"")
