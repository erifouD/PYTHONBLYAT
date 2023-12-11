def input_fruit():
    name = input("Введите название фрукта: ")
    quantity = int(input("Введите количество фруктов: "))
    return name, quantity
# Инициализация данных о фруктах на складе
fruit_inventory = {
    (1, 'Абрикос'): (30, 120),
    (1, 'Авокадо'): (19, 90),
    (1, 'Алыча'): (32, 67),
    (1, 'Апельсин'): (67, 129),
    (1, 'Арбуз'): (129, 19),
    (2, 'Гранат'): (36, 56),
    (2, 'Грейпфрут'): (23, 78),
    (2, 'Груша'): (57, 20),
    (2, 'Дыня'): (48, 45),
    (2, 'Инжир'): (12, 54),
    (2, 'Кешью'): (31, 73),
}
# Инициализация товаров в магазине
store_items = {
    'Апельсин': {'В наличии': 12, 'Необходимо': 20},
    'Груша': {'В наличии': 3, 'Необходимо': 10},
    'Арбуз': {'В наличии': 23, 'Необходимо': 35},
    'Авокадо': {'В наличии': 2, 'Необходимо': 8},
    'Дыня': {'В наличии': 0, 'Необходимо': 14},
}
# Заявки на каждый склад
warehouse_orders = {}
for (warehouse, fruit), (available_quantity, _) in fruit_inventory.items():
    # Проверка, что товар есть в магазине
    if fruit in store_items:
        # Получение данных о фрукте из магазина
        in_stock = store_items[fruit]['В наличии']
        needed = store_items[fruit]['Необходимо']
        # Оформление заявки
        order_quantity = min(available_quantity, needed)
        if order_quantity > 0:
            if warehouse not in warehouse_orders:
                warehouse_orders[warehouse] = []
            warehouse_orders[warehouse].append({'Фрукт': fruit, 'Количество': order_quantity})
            # Обновление данных в магазине
            store_items[fruit]['Необходимо'] -= order_quantity
            store_items[fruit]['В наличии'] -= order_quantity
# Вывод заявок на склады
for warehouse, orders in warehouse_orders.items():
    print(f"\nЗаявка для склада {warehouse}:")
    for order in orders:
        print(f"{order['Фрукт']} - {order['Количество']} кг")
