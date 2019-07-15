"""制作匹萨"""
def make_pizza(size, *toppings):
    print('我们将使用下面的配料制作一个' + str(size) + '寸的匹萨.')
    for topping in toppings:
        print(topping)
