# import pizza
#
# pizza.make_pizza(16,'辣椒')


# from pizza import make_pizza """使用这种导入方法,使用函数时不用再使用时句点调用函数了"""
#
# make_pizza(16,'辣椒')

from pizza import make_pizza as mp """重命名函数"""

mp(16,'青辣椒')