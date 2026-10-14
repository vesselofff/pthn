def caesar_cipher(text, shift):
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)

    return "".join(result)
