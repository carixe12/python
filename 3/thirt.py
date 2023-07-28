shop = [['BB', 1200], ['Crank', 1000], ['Saddle', 300], ['Pedal', 100], ['Saddle', 1500], ['Frame', 12000] , ['rim', 2000], ['crank', 200], ['saddle', 2700]]

part_name = input("Part name: ").capitalize()
total_cost = 0
count = 0

for part in shop:
    if part[0].capitalize() == part_name:
        count += 1
        total_cost += part[1]

print("Number of parts: ", count)
print("Total cost: ", total_cost)

