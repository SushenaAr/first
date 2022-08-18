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



def files(files):
    path= "C:\e"
    a= os.listdir(path)
    for file in files:
        if file in a:
            with open(file, encoding= 'utf-8') as f, open('fw.txt', 'a', encoding= 'utf-8') as fw:
                count= 0
                list_files= []
                for line in f:
                    count +=1
                    list_files.append(f"Строка номер {count} файла номер {file}\n")
                fw.write(f'\n{file}\n{count}\n{list_files}')
files(['1.txt','2.txt','3.txt'])









