cook_book = {}

def read_menu():

  with open ('Eat_list.txt') as eat_list:
    for line in eat_list:
      name = line.strip()
      num = int(eat_list.readline())
      cook_book.setdefault(name,[])
      for loop in range(num):
        ing = eat_list.readline().strip().split(' | ')
        cook_book[name].append({'ingridient_name':ing[0],
        'quantity':int(ing[1]), 'measure':ing[2]})
      eat_list.readline()


dishes = []
person_count =()

def get_shop_list_by_dishes(dishes, person_count):

  dich_dict = {}
  for food_name in dishes:
    for ingrid in cook_book.get(food_name):
      all_data = {'quantity':ingrid.get('quantity')*person_count,
      'measure':ingrid.get('measure')}

      if ingrid.get('ingridient_name') in dich_dict:
        name_ingr = ingrid.get('ingridient_name')
        quantity = dich_dict.get(name_ingr).get('quantity') \
          + ingrid.get('quantity')*person_count
        dich_dict.update({name_ingr:{'quantity':quantity,
          'measure':ingrid.get('measure')}})

      dich_dict.setdefault(ingrid.get('ingridient_name'), all_data)

  print(dich_dict, sep = '\n')

read_menu()
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)