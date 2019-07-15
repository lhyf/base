
""" 关键字 with 在不再需要访问文件后将其关闭 """

with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

with open('pi_digits.txt') as file:
    for line in file:
        print(line.rstrip())


with open('pi_digits.txt') as pi:
    lines = pi.readlines()
    print(lines)


for line in lines:
    print(line.rstrip())