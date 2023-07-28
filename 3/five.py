violator_songs = [
    ['World in My Eyes', 4, 86],
    ['Sweetest Perfection', 4, 43],
    ['Personal Jesus', 4, 56],
    ['Halo', 4, 9],
    ['Waiting for the Night', 6, 7],
    ['Enjoy the Silence', 4, 20],
    ['Policy of Truth', 4, 76],
    ['Blue Dress', 4, 29],
    ['Clean', 5, 83]
]

n = int(input("How many songs to choose? "))
selected_songs = []
total_time = 0

for i in range(n):
    title = input(f"{i+1}st song title: ")
    for song in violator_songs:
        if song[0] == title:
            selected_songs.append(song)
            total_time += song[1] + song[2]/100
            break
    else:
        print(f"Song '{title}' not found in the list of songs.")

print(f"The total playing time of the songs is {total_time:.2f} minutes")