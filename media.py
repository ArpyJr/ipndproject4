import webbrowser

class Video():
"""this is the parent class for classes Movie and TV"""
	def __init__(self, title, duration, release_date, trailer_url):
		self.title = title
		self.duration = duration
		self.release_date = release_date
		self.trailer_url = trailer_url

	def play_trailer():
	#function for playing the video trailer
		webbrowser.open(self.trailer_url)

class Movie(Video):
"""this is child class of Video for movies"""
	def __init__(self, title, duration, release_date, trailer_url,	box_office):
		Video.__init__(self, title, duration, release_date, trailer_url)
		self.box_office = box_office

class TV(Video):
"""this is child class of Video for TV shows"""
	def __init__(self, title, duration, release_date, trailer_url, num_seasons, num_episodes):
		Video.__init__(self, title, duration, release_date, trailer_url)
		self.num_seasons = num_seasons
		self.num_episodes = num_episodes