f = open("text.txt", "w+t")
f.write("Hello\n")
f.seek(0)
content = f.read()
print(content.strip())  

f.close()
