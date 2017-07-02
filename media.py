import webbrowser


class Movie():
    """ Use the Movie Class to create Movie instances """

    """ Send Movie Title, Storyline, a URL to
    the Poster image and youtube trailer """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ Open the Browser using and play
    the current instance's Movie Trailer """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
