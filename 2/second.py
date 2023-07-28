
names = ['claudio', 'evandor', 'alina', 'Gosha', 'Dima', 'paula', 'nada']


even_names = []


for i in range(len(names)):
    
    if i % 2 == 0:
        
        even_names.append(names[i])


print("First day:", even_names)