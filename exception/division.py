# try:
#     i = 5/0
# except ZeroDivisionError:
#     print("除数不能为0")
#################################

print("请输入两个数,我将计算他们的商")
while True:
    i = input('请输出被除数: ')
    if i == 'q':
        break

    j = input('请输入除数: ')
    if j == 'q':
        break
    try:
        answer = int(i) / int(j)
    except ZeroDivisionError:
        print("除数不能为0!")
    else:
        print("答案是:" + str(answer))
