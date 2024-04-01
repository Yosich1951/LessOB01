"""
В этом примере кода мы создали класс `Store`, который можно использовать
для управления магазинами.
В классе определены методы для добавления товара в ассортимент,
его удаления, обновления цен и получения цены товара.
Созданы три разных магазина с разным ассортиментом товаров. Д
ля одного из магазинов были протестированы все методы:
добавление товара, обновление цены, удаление товара из ассортимента и з
апрос цены на конкретный товар.

"""


class Store:
    """Класс для представления магазина."""

    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым словарем товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Метод для добавления товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Метод для удаления товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Метод для получения цены товара по его названию. Возвращает None, если товар отсутствует."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Метод для обновления цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание объектов класса Store
store1 = Store("Продукты 24", "ул. Новая, 15")
store2 = Store("Электроника Plus", "пр. Строителей, 28")
store3 = Store("Домашний Уют", "ул. Садовая, 3")

# Добавление товаров в ассортимент магазина
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("smartphone", 250)
store2.add_item("laptop", 1200)
store3.add_item("pillow", 15)
store3.add_item("blanket", 30)

# Протестируем методы на одном из магазинов
# Добавление товара
store1.add_item("oranges", 0.8)
print(store1.items)  # Проверяем добавление

# Обновление цены товара
store1.update_price("apples", 0.55)
print(store1.get_price("apples"))  # Смотрим новую цену

# Удаление товара
store1.remove_item("bananas")
print(store1.items)  # Проверяем состояние ассортимента после удаления

# Запрос цены товара
print(store1.get_price("milk"))  # Должно вернуть None, т.к. товара нет
