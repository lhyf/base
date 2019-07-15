class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + ' is now sitting.')

    def roll_over(self):
        print(self.name + ' rolled over!')

my_dog = Dog('小花',27)
print("my dog name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age) + " years old" )
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('YF', 27)
print("my dog name is " + your_dog.name.title() + ".")
print("my dog is " + str(your_dog.age) + " years old")
your_dog.sit()
your_dog.roll_over()