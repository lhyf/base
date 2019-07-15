import json

file_name = 'a.json'
numbers = [1,2,3,4,5,6,7,8,9]
with open(file_name,'w') as file:
    json.dump(numbers,file)


with open(file_name,'r') as file:
    numbers2 = json.load(file)

print(numbers2)