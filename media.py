#!/usr/bin/env python
print("Content-type:text/html \n")
import webbrowser

class Movie():
      VALID_RATINGS=["EXCELLENT","GOOD","BAD","AVERAGE"]
      
      def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
           self.title=movie_title
           self.storyline=movie_storyline
           self.poster_image_url=poster_image
           self.trailer_youtube_url=trailer_youtube
      def show_traiiler(self):
          webbrowser.open(self.trailer_youtube_url)
