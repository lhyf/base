def describe_pet(type, name='xiaobai'):
    print('\nI have a ' + type + '.')
    print("My " + type + "'s name is " + name.title() + ".")


describe_pet('dog', 'xiaoxed')

"""传递任意数量的实参(封装成元组传入)"""
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('AA', 'BB', 'CC')

"""使用任意数量的关键字实参(封装成字典传入)"""
def build_profile(first, last, **user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['姓'] = first
    profile['名'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


profiles = build_profile('李', '小花', 年龄=27, 性别='女')
print(profiles)
