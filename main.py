from PIL import Image

file = Image.open('qwe.png')

max_size_kb = 40


print(file.size)
print(file.size[0] * file.size[1])
print(file.size[0] * file.size[1] > max_size_kb * 1024)