import webbrowser

class Video():
"""this is the parent class for classes Movie and TV"""
	def __init__(self, title, image_url, trailer_url):
		self.title = title
		self.image_url = image_url
		self.trailer_url = trailer_url

	def play_trailer():
	#function for playing the video trailer
		webbrowser.open(self.trailer_url)

class Movie(Video):
"""this is child class of Video for movies"""
	print "Movie constructor Called"
	def __init__(self, title, image_url, trailer_url, box_office, release_date, duration):
		Video.__init__(self, title, image_url, trailer_url)
		self.box_office = box_office
		self.release_date = release_date
		self.duration = duration

class TV(Video):
"""this is child class of Video for TV shows"""
	print "TV constructor Called"
	def __init__(self, title, image_url, trailer_url, num_seasons, num_episodes,
				 first_episode, last_episode):
		Video.__init__(self, title, image_url, trailer_url)
		self.num_seasons = num_seasons
		self.num_episodes = num_episodes
		self.first_episode = first_episode
		self.last_episode = last_episode