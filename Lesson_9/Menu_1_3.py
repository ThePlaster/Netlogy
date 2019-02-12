def menu():
  cook_book = {}
  cook_dict = {}

  with open ('Eat_list.txt') as eat_list:
    for line in eat_list:
      name = line.strip()
      num = int(eat_list.readline())
      cook_dict.setdefault(name,[])
      for loop in range(num):
        cook_dict[name].append(eat_list.readline().replace('\n','').split(' | '))
      eat_list.readline()


  for name_eat, ingrid in cook_dict.items():
    cook_book.setdefault(name_eat, [])
    for loop in ingrid:
      cook_book[name_eat].append({'ingridient_name':loop[0],
      'quantity':loop[1], 'measure':loop[2]})

  dishes = []
  person_count =()
  dish_dict = {}

  def get_shop_list_by_dishes(dishes, person_count):

    for food_name in dishes:
      help_list = {}

      for key in cook_book.get(food_name):
        help_list = key.pop('ingridient_name')
        key['quantity'] = int(key.get('quantity')) * person_count
        if  help_list in dish_dict:
          quant_dich = int(dish_dict.get(help_list).get('quantity'))
          key['quantity'] = quant_dich + int(key.get('quantity'))
          dish_dict.update({help_list: key})
        else:
          dish_dict.setdefault(help_list, key)

    print(*dish_dict.items(), sep = '\n')

  get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

menu()
