import os
import webbrowser


html_head = '''
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Favorite Movies and TVs</title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script>
		window.onload = function () {
			$(".poster").mouseenter(function() {
				console.log("mouse entered");
				$(this).css("display", "none");
				$(this).siblings(".description").css("display", "block");
			});
			$(".description").mouseleave(function() {
				console.log("mouse left");
				$(this).css("display", "none");
				$(this).siblings(".poster").css("display", "block");
			});
			$("#video-box").click(function() {
				$(this).css("display", "none");
				$(this).empty();
			});
		}

		function launchTrailer(url) {
			$("#video-box").append('<iframe width="" height="" src=' + url + ' frameborder="0" allowfullscreen></iframe>');
			$("#video-box").css("display", "block");
		}
		</script>
		<style>
			body {
				width: 100%;
				height: 100%;
				margin: 0;
				position: relative;
			}

			#content-box {
				display: flex;
				flex-wrap: wrap;
				margin: 0;
				height: 100%;
				width: 100%;
			}

			.content {
				margin: 15px auto 15px auto;
				width: 400px;
				height: 600px;
				-webkit-box-shadow: 10px 10px 41px -13px rgba(0,0,0,0.75);
				-moz-box-shadow: 10px 10px 41px -13px rgba(0,0,0,0.75);
				box-shadow: 10px 10px 41px -13px rgba(0,0,0,0.75);
			}

			.poster {
				height: 100%;
				width: 100%;
			}

			.description {
				display: none;
				width: 100%;
				height: 100%;
			}

			#video-box {
				position: absolute;
				top: 0;
				display: none;
				z-index: 9;
				background: rgba(0, 0, 0, 0.70);
				height: 100%;
				width: 100%;
			}

			iframe {
				margin-left: 10vw;
				margin-top: 10vh;
				width: 80vw;
				height: 80vh;
			}
		</style>
	</head>
'''

html_body = '''
	<body>
		<div id="content-box">
			<!--
			This is the format for the content that will be displayed.
			Number of div.content should depend on number of Movie and TV instances.
			<div class="content">
			</div>
			-->
			<!-- example for Movie instance
			<div class="content">
				<img class="poster" src="https://s-media-cache-ak0.pinimg.com/564x/fd/5e/66/fd5e662dce1a3a8cd192a5952fa64f02.jpg" alt="title of video">
				<div class="description">
					<h1>Fight Club</h1>
					<h2>Length</h2>
					<p>125min</p>
					<h2>Release Date</h2>
					<p>October 32 2029</p>
					<h2>Director</h2>
					<p>TobyDoby Lemon</p>
					<h2>Box Office</h2>
					<p>&#36;20 Million</p>
					<a onclick="launchTrailer('https://www.youtube.com/embed/WNhH00OIPP0')">Play Trailer</a>
				</div>
			</div>
			-->
			<!-- example for TV instance
			<div class="content">
				<img class="poster" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd0NVxLFYMRfhJIjryxq6G-rWYQiqUnTf7bZmjwIgWA8HNUHXo" alt="title of video">
				<div class="description">
					<h1>Rick and Morty</h1>
					<h2>Network</h2>
					<p>Adult Swim</p>
					<h2>First Episode</h2>
					<p>February 31 2001</p>
					<h2>Last Episode</h2>
					<p>On going</p>
					<h2>Number of Seasons</h2>
					<p>3</p>
					<h2>Number of Episodes</h2>
					<p>22</p>
					<a onclick="launchTrailer('https://www.youtube.com/embed/WNhH00OIPP0')">Play Trailer</a>
				</div>
			</div>
			-->
			{content_goes_here}
		</div>
		<div id="video-box">
			<!-- trailer video format
			<iframe width="560" height="315" src="https://www.youtube.com/embed/WNhH00OIPP0" frameborder="0" allowfullscreen></iframe>
			-->
		</div>
	</body>
</html>
'''

movie_title_content = '''
<div class="content">
	<img class="poster" src="{poster_url}" alt="{movie_title}">
	<div class="description">
		<h1>{movie_title}</h1>
		<h2>Length</h2>
		<p>{duration}</p>
		<h2>Release Date</h2>
		<p>{release_date}</p>
		<h2>Director</h2>
		<p>{director}</p>
		<h2>Box Office</h2>
		<p>{box_office}</p>
		<a onclick="launchTrailer('{trailer_url}')">Play Trailer</a>
	</div>
</div>
'''

tv_title_content = '''
<div class="content">
	<img class="poster" src="{poster_url}" alt="{tv_title}">
	<div class="description">
		<h1>{tv_title}</h1>
		<h2>Network</h2>
		<p>{network}</p>
		<h2>First Episode</h2>
		<p>{first_episode}</p>
		<h2>Last Episode</h2>
		<p>{last_episode}</p>
		<h2>Number of Seasons</h2>
		<p>{number_of_seasons}</p>
		<h2>Number of Episodes</h2>
		<p>{number_of_episodes}</p>
		<a onclick="launchTrailer('{trailer_url}')">Play Trailer</a>
	</div>
</div>
'''

def create_content(video):
#spits out html content for movies and TVs
	content = ''
	for vid in video:
		if vid.vid_type == 'movie':
			content += movie_title_content.format(
				poster_url = vid.image_url,
				movie_title = vid.title,
				duration = vid.duration,
				release_date = vid.release_date,
				director = vid.director,
				box_office = vid.box_office,
				trailer_url = vid.trailer_url
			)
		elif vid.vid_type == 'tv':
			content += tv_title_content.format(
				poster_url = vid.image_url,
				tv_title = vid.title,
				network = vid.tv_network,
				first_episode = vid.first_episode,
				last_episode = vid.last_episode,
				number_of_seasons = vid.num_seasons,
				number_of_episodes = vid.num_episodes,
				trailer_url = vid.trailer_url
			)
		else:
			None
	return content

def create_html(video):
	#creates movies.html file
	output_file = open('movies.html', 'w')

	#addes movies and TVs content to the body of html
	output_html = html_body.format(content_goes_here = create_content(video))

	#writes head and body of html to movies.html
	output_file.write(html_head + output_html)
	output_file.close()

	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2)