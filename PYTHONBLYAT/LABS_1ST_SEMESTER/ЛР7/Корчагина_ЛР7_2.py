def input_fruit():
    name = input("Введите название фрукта: ")
    quantity = int(input("Введите количество фруктов: "))
    return name, quantity
# Инициализация данных о фруктах на складе
fruit_inventory = {
    'Абрикос': {'Склад': 1, 'Вес': 30, 'Цена за 1 кг': 120},
    'Авокадо': {'Склад': 1, 'Вес': 19, 'Цена за 1 кг': 90},
    'Алыча': {'Склад': 1, 'Вес': 32, 'Цена за 1 кг': 67},
    'Апельсин': {'Склад': 1, 'Вес': 67, 'Цена за 1 кг': 129},
    'Арбуз': {'Склад': 1, 'Вес': 129, 'Цена за 1 кг': 19},
    'Гранат': {'Склад': 2, 'Вес': 36, 'Цена за 1 кг': 56},
    'Грейпфрут': {'Склад': 2, 'Вес': 23, 'Цена за 1 кг': 78},
    'Груша': {'Склад': 2, 'Вес': 57, 'Цена за 1 кг': 20},
    'Дыня': {'Склад': 2, 'Вес': 48, 'Цена за 1 кг': 45},
    'Инжир': {'Склад': 2, 'Вес': 12, 'Цена за 1 кг': 54},
    'Кешью': {'Склад': 2, 'Вес': 31, 'Цена за 1 кг': 73},
}
# Инициализация товаров в магазине
store_items = {
    'Апельсин': {'В наличии': 12, 'Необходимо': 20},
    'Груша': {'В наличии': 3, 'Необходимо': 10},
    'Арбуз': {'В наличии': 23, 'Необходимо': 35},
    'Авокадо': {'В наличии': 2, 'Необходимо': 8},
    'Дыня': {'В наличии': 0, 'Необходимо': 14},}
# Заявки на каждый склад
warehouse_orders = {}
# Цикл оформления заявок
for position in range(1, len(store_items) + 1):
    print(f"\nЗаявка для склада {position}:")    
    while True:
        name, quantity = input_fruit()
        if name not in fruit_inventory:
            print("Такого фрукта нет на складе. Пожалуйста, выберите другой.")
            continue
        available_quantity = fruit_inventory[name]['Вес']
        max_weight_per_order = 30
        # Рассчитываем вес заказа
        order_quantity = min(quantity, available_quantity, max_weight_per_order)
        if name in warehouse_orders:
            warehouse_orders[name]['Вес'] += order_quantity
        else:
            warehouse_orders[name] = {'Вес': order_quantity, 'Цена за 1 кг': fruit_inventory[name]['Цена за 1 кг']}
        # Обновляем данные на складе
        fruit_inventory[name]['Вес'] -= order_quantity
        more_orders = input("Хотите добавить еще фрукты? (Да/Нет): ")
        if more_orders.lower() != 'Да':
            break
# Вывод информации о заявках
print("\nРезультирующий список в виде словаря:")
for fruit, order_details in warehouse_orders.items():
    print(f"{fruit}:")
    print(f"  Вес: {order_details['Вес']} кг")
    print(f"  Цена за 1 кг: {order_details['Цена за 1 кг']}")
