months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num = int(input("Vvedite mesyac"))

if num in [12, 1, 2]:
    print("Winter")
elif num in [3, 4, 5]:
    print("Spring")
elif num in [6, 7, 8]:
    print("Summer")
else:
    print("Autumn")
