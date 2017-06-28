import webbrowser

class Video():
	'''this is the parent class for classes Movie and TV'''
	def __init__(self, vid_type, title, image_url, trailer_url):
		self.vid_type = vid_type
		self.title = title
		self.image_url = image_url
		self.trailer_url = trailer_url

	def play_trailer(self):
	#function for playing the video trailer
		webbrowser.open(self.trailer_url)

class Movie(Video):
	'''this is child class of Video for movies'''
	def __init__(self, vid_type, title, image_url, trailer_url, box_office, release_date, duration, director):
		print "Movie constructor called"
		Video.__init__(self, vid_type, title, image_url, trailer_url)
		self.box_office = box_office
		self.release_date = release_date
		self.duration = duration
		self.director = director

class TV(Video):
	'''this is child class of Video for TV shows'''
	def __init__(self, vid_type, title, image_url, trailer_url, num_seasons, num_episodes,
				 first_episode, last_episode, tv_network):
		print "TV constructor called"
		Video.__init__(self, vid_type, title, image_url, trailer_url)
		self.num_seasons = num_seasons
		self.num_episodes = num_episodes
		self.first_episode = first_episode
		self.last_episode = last_episode
		self.tv_network = tv_network