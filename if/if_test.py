car = True
if car == False:
    print(car)
else:
    print("不相等")

carList = ['bmw', 'audi', 'benz']
for car in carList:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

available_topping = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fires', 'extra cheese']

for requested in requested_toppings:
    if requested in available_topping:
        print("Adding " + requested)
    else:
        print("我们没有" + requested)

msg = input("说点什么吧 \n输入quit 退出 \n")
msg = ""
while msg != "quit":
    msg = input("再输入些什么吧")
    if msg != 'quit':
        print(msg)
