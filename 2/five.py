
n = int(input("Number of containers: "))


container_weights = []


for i in range(n):
    weight = int(input("Enter container weight: "))
    
    if weight > 200:
        print("Error: Container weight exceeds 200.")
        exit()
    container_weights.append(weight)


new_weight = int(input("Enter new container weight: "))

if new_weight > 200:
    print("Error: Container weight exceeds 200.")
    exit()

container_weights.append(new_weight)

container_weights.sort(reverse=True)

position = container_weights.index(new_weight) + 1

print("The number that the new container will receive:", position)