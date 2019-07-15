from collections import OrderedDict

favorite_language = OrderedDict()
favorite_language['xiaohong'] = 'Java'
favorite_language['xiaohua'] = 'Python'
favorite_language['yf'] = 'C++'

for name,language in favorite_language.items():
    print("姓名:" + name.title() + " 喜欢的语言是: " + language)