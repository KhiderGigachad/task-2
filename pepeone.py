import os.path
import os
import codecs
from sys import getdefaultencoding
getdefaultencoding()
cook_book = {}

with open('recipes', 'rt', encoding="utf-8") as file:
	for l in file:
		department_name = l.strip()
		diction = []
		count = file.readline()
		for i in range(int(count)):
			emp = file.readline()
			ingredient_name, quantity, measure  = emp.strip().split(' | ')
			diction.append({'ingredient_name': ingredient_name,
                                     'quantity': (int(quantity)),
                                     'measure': measure})
			dep = {department_name: diction}
		blank_line = file.readline()
		cook_book.update(dep)
# print(f'cook_book = {cook_book}')



def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
# print(get_shop_list_by_dishes(4, ['Фахитос', 'Утка по-пекински']))


def myFunc(e):
  with open ((e),'r',encoding='utf-8') as f:
    return len(f.readlines())

count = []
path = r'C:\Users\KhiderS\Desktop\pepeone\task 2'

for i in os.listdir():
  if i.endswith('.txt'):
    count.append(i)

count.sort(key=myFunc)

with open(r'C:\Users\KhiderS\Desktop\pepeone\task 2\txt4.txt','w', encoding='utf-8', errors='ignore') as f:
	for j in count:
		if j != "txt4.txt":
			s = open(j,'r',encoding='utf-8').read()	
			f.write(j)
			f.write('\n')

			f.write(str(s.count("\n") + 1))
			f.write('\n')

			f.write(s)
			f.write('\n')	



