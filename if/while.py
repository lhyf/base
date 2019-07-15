# while True:
#     msg = input("请输入你要添加到匹萨中的配料: ")
#
#     if msg == 'quit':
#         break
#     else:
#         print("我们会将" + msg + "添加到匹萨中")
#

sandwich_orders = ['A','B','C']
finished_shandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop();
    print('I made your sandwich, ' + sandwich)

    finished_shandwiches.append(sandwich)

print('三明治已经做好啦')
for sandwich in finished_shandwiches:
    print(sandwich + '.')


def greet_user():
    """用三个双引号,包起来,形成文档字符串的注释"""
    print("Hello World!")

greet_user()


