from collections import Counter
# Создаём пустой объект Counter
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter()
for car in cars:
    c[car]+= 1
    print(c)
    c = Counter(cars)
    #Узнать, сколько раз встретился конкретный элемент, можно, обратившись к счётчику по ключу как к обычному словарю:
print(c['black'])
#Узнать сумму всех значений в объекте Counter можно, воспользовавшись следующей конструкцией:
print(sum(c.values()))
#Увидеть только уникальные значения из списка
print(list(c))
#Преобразовывание в словарь
print(dict(c))
#Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print(c.most_common)
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
Counter_moscow = Counter(cars_moscow)
Counter_spb = Counter(cars_spb)
print(Counter_spb)
print(Counter_moscow)
#Сложение двух счетчиков
Counter_all = Counter_moscow+Counter_spb
print(Counter_all)
#Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract,
b = Counter_moscow - Counter_spb 
print(Counter_moscow)
c = Counter_moscow.subtract(Counter_spb)
print(Counter_moscow)
Counter_spb.clear
Counter_all.clear
Counter_moscow.clear
from collections import Counter
clients = [953421196, 953421161, 953421142, 953421186, 953421181, 953421144, 953421190, 953421184, 953421141, 953421193, 953421129, 953421158, 953421130, 953421177, 953421181, 953421136, 953421160, 953421184, 953421146, 953421175, 953421110, 953421139, 953421100, 953421116, 953421130, 953421179, 953421181, 953421136, 953421174, 953421167, 953421132, 953421195, 953421145, 953421108, 953421143, 953421133, 953421180, 953421149, 953421135, 953421195, 953421143, 953421131, 953421157, 953421189, 953421128, 953421132, 953421127, 953421151, 953421197, 953421160, 953421112, 953421155, 953421182, 953421168, 953421131, 953421156, 953421113, 953421102, 953421113, 953421192, 953421142, 953421105, 953421165, 953421175, 953421102, 953421195, 953421154, 953421165, 953421141, 953421166, 953421126, 953421143, 953421165, 953421150, 953421187, 953421129, 953421176, 953421169, 953421109, 953421177, 953421109, 953421150, 953421136, 953421140, 953421189, 953421198, 953421186, 953421159, 953421184, 953421182, 953421133]
clients_counter = Counter(clients)
#print(clients.count(953421102))
#print(list(clients_counter))
#print(clients_counter.elements)
n = list(clients_counter)
print(clients_counter.most_common(1))
print(clients_counter[953421102])
print(len(list(clients_counter)))#Подсчет количество уникальных значений в списке clients

