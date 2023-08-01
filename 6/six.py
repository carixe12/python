n = int(input("Enter number of orders: "))

orders = {}
for i in range(n):
    order = input(f"Enter {i+1} order: ").split()
    customer = order[0]
    pizza = order[1]
    quantity = int(order[2])
    if customer in orders:
        if pizza in orders[customer]:
            orders[customer][pizza] += quantity
        else:
            orders[customer][pizza] = quantity
    else:
        orders[customer] = {pizza: quantity}
for customer in sorted(orders.keys()):
    print(customer + ":")
    for pizza, quantity in sorted(orders[customer].items()):
        print(pizza.capitalize() + ":", quantity)