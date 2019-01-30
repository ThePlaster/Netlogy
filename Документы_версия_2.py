
documents_list = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "passport", "number": "039032"},
  ]

directories_dict = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
  }


help_list = []

for loop in directories_dict.values():
  for loop_2 in loop:
    help_list.append(loop_2)


def peaple(docum):
  doc_list = []
  doc_num = str(input("Введите номер документа: "))

  for doc in documents_list:
    doc_list = [doc['number'], doc['name']]
    if doc_list[0] == doc_num:
      print('\nВладелец этого документа - ', doc_list[1])

  if doc_num not in help_list:
    print('\nДокумент с номером "{}" не найден!'.format(doc_num))
  return peaple


def data_list(print_type):
  for doc in documents_list:
    print('\nТип документа: "{}", номер: "{}", владелец: "{}"'
      .format(doc['type'], doc['number'], doc['name']))
  return data_list


def searh_shelf(directories_dict):
  doc_num = str(input("Введите номер документа: "))
  for key, num in directories_dict.items():
    for x in num:
      if x == doc_num:
        print('\nДокумент лежит на', key, 'полке')

  if doc_num not in help_list:
    print('\nДокумент с номером "{}" не найден!'.format(doc_num))
  return searh_shelf


def add_doc(documents_list):
  input_type = input('\nВведите тип документа: ')
  input_num = str(input('Введите номер документа: '))
  input_name = input('Введите фамилию и имя владельца документа: ')
  input_shelf = str(input('На какой полке будет храниться документ:  '))

  documents_list.extend([{'type': input_type, 'number': input_num, 'name': input_name}])

  if input_shelf in directories_dict.keys():
    for doc  in directories_dict.keys():
      if doc == input_shelf:
        doc_list = directories_dict.get(input_shelf)
        doc_list.append(input_num)
  else:
    directories_dict.setdefault(input_shelf, [input_num])

  print('\nСписок документов:')
  for doc in documents_list:
    print(doc)

  print('\nСписок хранящихся документов:')
  for doc in directories_dict.items():
    print(doc)
  return add_doc


def del_doc(documents_list):
  del_doc = str(input('Введите номер документа, который нужно удалить: '))
  for doc_list in documents_list:
    if del_doc in doc_list.values():
      documents_list.remove(doc_list)

  for doc_list in directories_dict.values():
    if del_doc in doc_list:
      doc_list.remove(del_doc)

  print('\nСписок документов:')
  for doc in documents_list:
    print(doc)

  print('\nСписок хранящихся документов:')
  for doc in directories_dict.items():
    print(doc)

  if del_doc not in help_list:
    print('\nДокумент с номером "{}" не найден!'.format(del_doc))
  return del_doc


def movement(directories_dict):
  input_num = str(input("Введите номер документа: "))
  input_direct = str(input("На какую полку переложить документ: "))

  if input_num not in help_list:
    print('\nДокумент с номером "{}" не найден!'.format(input_num))

  for doc in directories_dict.values():
    if input_num in doc and input_direct <= str(len(directories_dict)):
      doc_list = directories_dict.get(input_direct)
      doc_list.append(input_num)

  if input_direct in directories_dict.keys():
    for move in directories_dict.values():
      if input_num in move:
        move.remove(input_num)
  else:
    print('\nПолка №{} не найдена!'.format(input_direct))

  print('\nСписок хранящихся документов:')
  for doc in directories_dict.items():
    print(doc)
  return movement


def add_shelf(directories_dict):
  add_shelf = str(input('Введите номер новой полки: '))
  directories_dict.setdefault(add_shelf,[])

  print('\nСписок хранящихся документов:')
  for doc in directories_dict.items():
    print(doc)
  return add_shelf


def print_name(documents_list):
  print('')
  try:
    for name in documents_list:
      first_name, last_name = name['name'].split(' ')
      print(first_name)
    return print_name
  except KeyError:
    print('\nНе заполненно поле "name" у одного из владельцев')


def command_menu():

  print('Доступные операции:\n')
  print('p - people – узнать владельца документа по его номеру')
  print('l – list - вывести список всех документов')
  print('s – shelf - узнать на какой полке лежить документ, по его номеру')
  print('a – add - добавить новый документ')
  print('d – delete - удалить документ')
  print('m – move - переместить документ на другую полку')
  print('as – add shelf - добавить новую полку')
  print('n - name - вывести список имен владельцев документов')

  user_input = input('Введите букву(латиницей) для продолжения: ').lower()

  if user_input == 'p':
    peaple(documents_list)
  elif user_input == 'l':
    data_list(documents_list)
  elif user_input == 's':
    searh_shelf(directories_dict)
  elif user_input == 'a':
    add_doc(documents_list)
  elif user_input == 'd':
    del_doc(documents_list)
  elif user_input == 'm':
    movement(directories_dict)
  elif user_input == 'as':
    add_shelf(directories_dict)
  elif user_input == 'n':
    print_name(documents_list)
  else:
    print('\nВы ввели не корректные данные')


command_menu()


print('\nКонец программы!')
