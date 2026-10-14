def caesar_decrypt(text, shift):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            new_pos = (ord(ch) - base - shift) % 26
            result.append(chr(base + new_pos))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            new_pos = (ord(ch) - base - shift) % 26
            result.append(chr(base + new_pos))
        else:
            result.append(ch)
    return ''.join(result)

cipher = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for s in range(26):
    print(f"{s:2d}: {caesar_decrypt(cipher, s)}")
