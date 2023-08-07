with open('first_tour.txt', 'r') as f:
    lines = f.readlines()

k = int(lines[0])
participants = []

for line in lines[1:]:
    last_name, first_name, points = line.strip().split()
    points = int(points)
    if points > k:
        participants.append((last_name, first_name[0], points))

participants.sort(key=lambda x: x[2], reverse=True)

with open('second_tour.txt', 'w') as f:
    f.write(str(len(participants)) + '\n')
    for i, participant in enumerate(participants, 1):
        last_name, initial, points = participant
        f.write(f"{i}) {initial}. {last_name} {points}\n")