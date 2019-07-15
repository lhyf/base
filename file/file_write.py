
msg = 'msg.txt'

""" w:写入模式 r:读取模式 a:附加模式 r+:读取和写入 """
with open(msg,'a') as file:
    file.write('I Love You. \n')
    file.write('I Love LiXiaoHua. \n')


try:
    with open(msg,'r') as file:
        content = file.read()

except FileNotFoundError:
    pass
    # print("文件 " + msg + " 不存在.")

else:
    words = content.split()
    num_words = len(words)
    print("一共包含 " + str(num_words) + " 个词")