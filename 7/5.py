max_of_two = lambda a, b: a if a > b else b
print(max_of_two(10, 20))  # 20

mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
checks = [1 <= x <= 130 for x in mass]
print(checks)  # [True, True, False, True, False, True, True, False, True, True, False]

list_ = [10, 11, 14, 25, 33, 36, 100, 101]
odd_numbers = list(filter(lambda val: val % 2 != 0, list_))
print(odd_numbers)  # [11, 25, 33, 101]

files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']

sorted_files = sorted(files, key=lambda f: not f.endswith('.mp3'))
print(sorted_files)  
