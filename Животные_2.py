# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#     гусей "Серый" и "Белый" +
#     корову "Маньку"+
#     овец "Барашек" и "Кудрявый"+
#     кур "Ко-Ко" и "Кукареку" +
#     коз "Рога" и "Копыта"+
#     и утку "Кряква" +
# Со всеми животными вам необходимо как-то взаимодействовать:
#     кормить +
#     корову и коз доить+
#     овец стричь+
#     собирать яйца у кур, утки и гусей +
#     различать по голосам(коровы мычат, утки крякают и т.д.)+

# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование,
# определить общие методы взаимодействия с животными и дополнить их в дочерних классах,
# если потребуется.

# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить(+) и подоить/постричь/собрать яйца, если надо.+

# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).+
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

class HomeAnimal():
    state_eat = 'Low'
    species = ''
    state_act = ''
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.state_eat = 'Full'
        print('Вы покормили')


class HomeBird(HomeAnimal):
    def act(self):
        self.state_act = 'Яйца собраны!'


class Goose(HomeBird):
  species = 'Гусь'
  voice = 'Га-га-га'


class Chicken(HomeBird):
  species = 'Курица'
  voice = 'Ко-ко-ко'


class Duck(HomeBird):
  species = 'Утка'
  voice = 'Кря-кря'


class Ewe(HomeAnimal):
  species = 'Баран'
  voice = 'Беее'
  def act(self):
    self.state_act = 'Шерсть подстрижена!'

class Cow(HomeAnimal):
  species = 'Корова'
  voice = 'Му-му'

  def act(self):
    self.state_act = 'Молоко собрано!'

class Goat(HomeAnimal):
  species = 'Коза'

  voice = 'Меее'
  def act(self):
    self.state_act = 'Молоко собрано!'

goose_gray = Goose('Серый', 5)
goose_white = Goose('Белый', 4.5)
chicken_koko = Chicken('Ко-ко', 4.3)
chichen_kuka = Chicken('Кукареку', 4.7)
duck_kr = Duck('Кряква', 4)
ewe_baran = Ewe('Барашек', 65)
ewe_curly= Ewe('Кудрявый', 70)
goat_horn = Goat('Рога', 90)
goat_hoof = Goat('Копыта', 86)
cow = Cow('Мурка', 375)

animal_dict = {
  'Goose':[goose_gray, goose_white],
  'Chicken':[chicken_koko, chichen_kuka],
  'Duck':[duck_kr],
  'Ewe':[ewe_baran, ewe_curly],
  'Cow':[cow],
  'Goat':[goat_horn, goat_hoof]
  }


for animal in animal_dict.values():
  for loop in animal:
    loop.eat()
    print('{} {}! {} сказал(а): "{}" \n'.format(loop.species, loop.name,
     loop.species, loop.voice))

print('')

for animal, name in animal_dict.items():
    for loop in name:
      loop.act()
      print(loop.species, loop.name,
      'обслужен(а) - ', loop.state_act.lower())


the_heavy = 0
the_heavy_name = ''
the_heavy_spec = ''
summ_animal_weight = 0

print('')

for animal, weit in animal_dict.items():
    for loop in weit:
        summ_animal_weight += loop.weight
        print(loop.species, loop.name, 'весит',loop.weight, 'кг')
        if loop.weight > the_heavy:
            the_heavy = loop.weight
            the_heavy_name = loop.name
            the_heavy_spec = loop.species


print('\n')
print('Суммарный вес всех животных = ', summ_animal_weight, 'кг')
print(the_heavy_spec, the_heavy_name,
'самое тяжёлое живонтное, весит = ',the_heavy, 'кг')

print('\nEnd program')