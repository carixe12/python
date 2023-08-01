songs = {'World in My Eyes': 4.86,
         'Sweetest Perfection': 4.43,
         'Personal Jesus': 4.56,
         'Halo': 4.9,
         'Waiting for the Night': 6.07,
         'Enjoy the Silence': 4.20,
         'Policy of Truth': 4.76,
         'Blue Dress': 4.29,
         'Clean': 5.83}

num_songs = int(input("How many songs to choose? "))
selected_songs = []

for i in range(num_songs):
    song_title = input("Enter the title of song {}:".format(i + 1))
    selected_songs.append(song_title)

total_time = sum(songs[title] for title in selected_songs)

print("Total song time: {:.2f} minutes".format(total_time))