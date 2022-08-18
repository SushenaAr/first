from pprint import pprint
import os

with open("recipes.txt", encoding="utf-8") as file:
    cook_book = {}


    for line in file:
        recipe=[] 
        dish= line.strip() 
        quantity = int(file.readline().strip()) 
        for line in range(quantity):
            line_recipe = file.readline().split(" | ")
            recipe.append({'ingredient_name': line_recipe[0], 'quantity': int(line_recipe[1]), 'measure': line_recipe[2].strip()})
        cook_book[dish] = recipe 
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    recipe= {}
    for i in dishes:
        for a,b in cook_book.items():
            if i ==a:
                for c in b:                     
                    d= c['quantity']*person_count
                    recipe[c['ingredient_name']]= {'measure': c['measure'], 'quantity': d}                                
            else:
                continue
    pprint(recipe)
    return



def files():
    with open('1.txt', encoding= 'utf-8') as f1, open('2.txt', encoding= 'utf-8') as f2, open('fw.txt', 'a', encoding= 'utf-8') as fw:

        #т.к я знаю кол-во и названия файлов, могу обойтись без цикла, так с маленьким объемом мне кажется,
        # будет быстрее
        count_1= 0
        text_1=[]
        for line in f1:
            count_1+= 1
            text_1.append(f'строка номер {count_1} файла номер 1')

        count_2= 0
        text_2= []
        for line in f2:
            count_2+= 1
            text_2.append(f'строка номер {count_2} файла номер 2')

        #сравниваю, тут я даже не представляю сравнение по другому и если файлов будет больше двух
        a= count_1> count_2
        if a == True:
            fw.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                fw.write(f'{a}\n')
            fw.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                fw.write(f'{b}\n')
        else:
            fw.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                fw.write(f'{b}\n')
            fw.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                fw.write(f'{a}\n')

files()









