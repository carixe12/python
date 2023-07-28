
n = int(input("Number of graphics cards: "))

video_cards = []

for i in range(1, n+1):
    card = int(input("Video card {}: ".format(i)))
    video_cards.append(card)

if not video_cards:
    print("The list is empty.")
else:
    
    max_card = max(video_cards)

    while max_card in video_cards:
        video_cards.remove(max_card)

    print(video_cards)