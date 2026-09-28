filename = "inverted_sort.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

lines_stripped = [line.rstrip("\n") for line in lines]

reversed_lines = lines_stripped[::-1]

with open(filename, "a", encoding="utf-8") as f:
    f.write("\n")
    for line in reversed_lines:
        f.write(line + "\n")
