def year_name(year: int):

    animals = [
        "крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
        "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"
    ]

    colors = ["зеленый", "красный", "желтый", "белый", "черный" ]

    baseyr = 1984

    smesh = year - baseyr

    animals_inx = smesh % 12
    colors_inx = smesh % 5

    animal = animals[animals_inx]
    color = colors[colors_inx]

    return f"{color} {animal}"

try:
  useryr = int(input("Vvedite god: "))
  result = year_name(useryr)
  print(f"{useryr} year is year of {result}")
except ValueError:
  print("Err")
