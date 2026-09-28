num = input("Vvedite 4hznach chislo:")
if len(num) != 4:
    print("Error not 4 znach")

else:
    palindrom = num == num[::-1]
if palindrom:
       print(f"Verno {palindrom}")
else:
    print("Ne verno")
