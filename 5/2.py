def caesar_shift_char(ch: str, shift: int) -> str:
    if 'а' <= ch <= 'я':
        base = ord('а')
        offset = (ord(ch) - base - shift) % 32
        return chr(base + offset)
    elif 'А' <= ch <= 'Я':
        base = ord('А')
        offset = (ord(ch) - base - shift) % 32
        return chr(base + offset)
    else:
        return ch

def encrypt_line(line: str, shift: int) -> str:
    return ''.join(caesar_shift_char(ch, shift) for ch in line)

def main():
    input_file = "message.txt"
    output_file = "encrypted.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return

    encrypted_lines = []
    for i, line in enumerate(lines, start=1):
        shift = i  # 1-я строка на 1, 2-я на 2, ...
        encrypted_line = encrypt_line(line, shift)
        encrypted_lines.append(encrypted_line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(encrypted_lines)

    print(f"Шифрв в: {output_file}")

if __name__ == "__main__":
    main()
