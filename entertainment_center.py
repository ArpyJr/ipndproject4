import media

'''
Movie class format (self, title, image_url, trailer_url, box_office, release_date, duration, director)

TV class format    (self, title, image_url, trailer_url, num_seasons, num_episodes,
					first_episode, last_episode, tv_network)
'''

The_legend_of_1900 = media.Movie('The Legend of 1900', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Leggenda_pianista.jpg/220px-Leggenda_pianista.jpg',
								 'https://www.youtube.com/watch?v=2uf-LDlZMFE', '$259,127', 'October 28 1998', '125 minutes', 'Giuseppe Tornatore')

print The_legend_of_1900.duration