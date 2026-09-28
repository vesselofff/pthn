nomer = int(input("Vvedite nomer ot 1-5"))
mass = float(input("Vvedite massu"))

bok = {
    1: 1,
    2: 0.000001,
    3: 0.001,
    4: 1000,
    5: 10
}

if nomer in bok:
    result = mass*bok[nomer]
    print(f"Massa b kg {result}")
else:
    print("Err")
