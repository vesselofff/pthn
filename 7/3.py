import re

def numbers_to_letters(text: str) -> str:
    def replace_num(m):
        num = int(m.group())
        if 1 <= num <= 26:
            return chr(ord('a') + num - 1)
        if num == 0:
            return ''
        return m.group()

    replaced = re.sub(r'\d+', replace_num, text)

    result = []
    i = 0
    while i < len(replaced):
        ch = replaced[i]
        if ch == ' ':
            if result and i + 1 < len(replaced) and result[-1].isalpha() and replaced[i+1].isalpha():
                i += 1
                continue
        result.append(ch)
        i += 1

    return ''.join(result)

print(numbers_to_letters("8 5 12 12 15"))
print(numbers_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !"))
