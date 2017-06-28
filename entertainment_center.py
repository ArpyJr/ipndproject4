import media
import constructor

'''
Movie class format (self, title, image_url, trailer_url, box_office, release_date, duration, director)

TV class format    (self, title, image_url, trailer_url, num_seasons, num_episodes,
					first_episode, last_episode, tv_network)

'''
#MOVIE
the_legend_of_1900 = media.Movie('movie', 'The Legend of 1900', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Leggenda_pianista.jpg/220px-Leggenda_pianista.jpg',
								 'https://www.youtube.com/embed/2uf-LDlZMFE', '$259,127', 'October 28 1998', '125 minutes', 'Giuseppe Tornatore')

dr_strangelove = media.Movie('movie', 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb',
							 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Dr._Strangelove_poster.jpg/220px-Dr._Strangelove_poster.jpg',
							 'https://www.youtube.com/embed/1gXY3kuDvSU', '$9.4 million', 'January 29 1964', '94 minutes', 'Stanley Kubrick')

cloud_atlas = media.Movie('movie', 'Cloud Atlas', 'https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg',
						  'https://www.youtube.com/embed/hWnAqFyaQ5s', '$130.5 million', 'October 26 2012', '171 minutes',
						  'Lana Wachowski, Tom Tykwer, Andy wachowski')

#TV
dexter = media.TV('tv', 'Dexter', 'http://www.gstatic.com/tv/thumb/tvbanners/9707531/p9707531_b_v8_aa.jpg', 'https://www.youtube.com/embed/YQeUmSD1c3g',
				  8, 96, 'October 1 2006', 'September 22 2013', "Showtime")

rick_and_morty = media.TV('tv', 'Rick and Morty', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI30BIvWf2gh_Qr3-ksjb83DrCbivewBoHhzM3Hww5HB7DSuLa8Xybfg',
						  'https://www.youtube.com/embed/WNhH00OIPP0', 3, 22, 'December 2 2013', 'present', 'Adult Swim')

narcos = media.TV('tv', 'Narcos', 'http://www.gstatic.com/tv/thumb/tvbanners/12985822/p12985822_b_v8_ab.jpg', 'https://www.youtube.com/embed/U7elNhHwgBU',
				  2, 20, 'August 28 2015', 'present', 'Netflix')

videos = [the_legend_of_1900, dr_strangelove, cloud_atlas, dexter, rick_and_morty, narcos]

constructor.create_html(videos)