import random
import pickle
import os

_dict = {'False': 'Логическое значение', 'None': 'Пустой'}
keys = list(_dict.keys())
ind = random.randint(0, len(keys) - 1)
secret = keys[ind]
mask = [' * '] * len(secret)

SAVE_FILE = "game_state.pkl"

def save_game():
    state = {
        "secret": secret,
        "mask": mask
    }
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(state, f)
    print("Игра сохранена!")

def load_game():
    global secret, mask
    if not os.path.exists(SAVE_FILE):
        print("Нет сохранённой игры.")
        return False

    try:
        with open(SAVE_FILE, "rb") as f:
            state = pickle.load(f)
        secret = state["secret"]
        mask = state["mask"]
        print("Игра загружена!")
        return True
    except (EOFError, pickle.UnpicklingError):
        print("Ошибка при загрузке файла — сохранение повреждено.")
        return False

def show_describe():
    """Выводит описание слова."""
    print(_dict[secret])

def show_secret():
    """Выводит текущее состояние загаданного слова."""
    for val in mask:
        print(val, end="")
    print()

def get_letter():
    letter = input("\nВведите букву: ")
    return letter

def check_letter(letter):
    for idx, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[idx] = f" {letter} "

def start():
    # Сначала пробуем загрузить сохранение
    if load_game():
        print("Продолжаем ранее начатую игру.")
    else:
        # Если нет сохранения — начинаем новую
        print("Начинаем новую игру.")

    while " * " in mask:
        show_describe()
        show_secret()
        letter = get_letter()
        check_letter(letter)

        save_game()

start()
