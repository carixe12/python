goods = {
    'Lamp': '12345',
    'Table': '23456',
    'Sofa': '34567',
    'Chair': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item, code in goods.items():
    total_quantity = 0
    total_cost = 0
    for item_info in store[code]:
        total_quantity += item_info['quantity']
        total_cost += item_info['quantity'] * item_info['price']
    print(f"{item} - {total_quantity} pieces, cost {total_cost} rubles.")