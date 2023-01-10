# 10.  Разработайте программу, имитирующую работу транспортного агентства.
# Транспортное агентство имеет сеть филиалов в нескольких городах.
# Транспортировка грузов осуществляется между этими городами тремя видами транспорта:
# автомобильным, железнодорожным и воздушным. Любой вид транспортировки имеет стоимость
# единицы веса на единицу пути и скорость доставки. Воздушный транспорт можно
# использовать только между крупными городами, этот вид самый скоростной и самый дорогой.
# Железнодорожный транспорт можно использовать между крупными и средними городами,
# этот вид самый дешевый. Автомобильный транспорт можно использовать между любыми городами.
# Заказчики через случайные промежутки времени обращаются в один из филиалов транспортного
# агентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки.
# Транспортное агентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
#
# -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
# -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
# -Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.
#
# from geopy import distance
#
#
# class City:
#     pass
#
# class Tranport:
#     def __init__(self, auto, avia,train, sity, distance):
#         self.auto = auto            # кол-во авто в городе
#         self.avia = avia            # кол-во самолетов в городе
#         self.train = train          # кол-во поездов в городе
#         self.sity = sity            # город
#         self.ditance = distance     # расстояние
#
#         if self.ditance > 300:
#             print(f'доставка ')
#
# class Minsk(City):
#     def garage(cls):
#         pass
#
#     @classmethod
#     def koordinat(cls):
#         dist = (53.9, 27.5667)
#         return dist
#
#
# class Vilnus(City):
#     @property
#     @classmethod
#     def koordinat(cls):
#         dist = (54.6892,25.2798)
#         return dist
#
# class Warsaw(City):
#     @property
#     @classmethod
#     def koordinat(cls):
#         dist = (52.2318, 21.0061)
#         return dist
#
#
# class Soligorsk(City):
#     @classmethod
#     def koordinat(cls):
#         dist = (52.7835, 27.5426)
#         return dist
#
# class Mogilev(City):
#     @classmethod
#     def koordinat(cls):
#         dist = (53.8942, 30.3303)
#         return dist
#
# class Brest(City):
#     @property
#     @classmethod
#     def koordinat(cls):
#         dist = (52.0966, 23.7040)
#         return dist
#
#
#
# class FinanceTA:
#     def distance_trevel(self, dest1: City, dest2: City):
#         dist = distance.geodesic(dest1, dest2).kilometers           # считает расстояние между городами
#         return dist
#
#     def cost(self,dest1,dest2,kg):
#         if self.distance_trevel(dest1,dest2)>=100 and kg <=20:
#             print(f'asd')
#
#
#
#
# TrancAg = FinanceTA()
# TrancAg.distance_trevel(Warsaw.koordinat, Vilnus.koordinat)


# class Calculator:
#
#     def init(self):
#         self._name = str()
#
#     @property
#     def name(self):
#         if Calculator.name().isalpha:
#             return self._name
#         else:
#             print('неправильно')
#
#     @classmethod
#     @name.setter
#     def name(self, name: str):
#         self._name = name
#
#
# a = Calculator()
# a.name = 234234
# print(a.name)



import sqlite3
conn = sqlite3.connect('shop_box.db')
cursor = conn.cursor()

class Goods:
    def __init__(self,name):
        self.name = name

    @classmethod
    def is_good(cls, name):
        good = cls(name)
        return good.good_select()

    def good_select(self):
        goods = cursor.execute("SELECT good_id, name FROM goods")
        for gd in goods:
            if gd[1] == self.name:
                return gd[0]
        else:
             return False


class Box:
    def add_goods(self,good,count):

        if Goods.is_good(good):
            cursor.execute("INSERT INTO box (good_id,count_good) VALUES(?,?)", (Goods.is_good(good), count))
            conn.commit()

    def del_goods(self, good):
        goods = cursor.execute("""
            SELECT goods.name, box.good_id FROM goods 
            INNER JOIN box USING (good_id)
            """ )

        for gd in goods:
            if gd[0] == good:
                cursor.execute("""DELETE FROM box WHERE box.good_id == ?""", (gd[1],))
                conn.commit()
                break


    def resize_count_good(self, good, count):
        goods = cursor.execute("""
                    SELECT goods.name, box.good_id FROM goods 
                    INNER JOIN box USING (good_id)
                    """)

        for gd in goods:
            if gd[0] == good:
                cursor.execute("""UPDATE box SET count_good = ? 
                                    WHERE good_id = ?""", (count, gd[1],))
                conn.commit()
                break
        else:
            print('no goods')

    def watch_box(self):
        goods = cursor.execute (""" 
                SELECT count_good FROM box
                INNER JOIN goods USING (name)
        """)

        for gd in goods:
            if gd in goods

class Costumer:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        self.box = Box()

    def get_good(self, good, count):
        self.box.add_goods(good,count)

    def del_goods(self, good):
        self.box.del_goods(good)

    def change_goods(self, good, count):
        self.box.resize_count_good(good, count)

    def view_box(self):





Vasia = Costumer('Vasia', 45, 560)
Vasia.change_goods('cheese', 8)









