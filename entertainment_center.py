import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story"," a story about toy",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


#print toy_story.storyline
avavtar = media.Movie("Avatar"," a story about alien planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print avavtar.title
#avavtar.show_tailer()

logan = media.Movie("Logan","a story about ... ",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
#logan.show_tailer()


ratatouille = media.Movie("Ratatouille","a story about a rat",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")



midnight_in_paris = media.Movie("Midnight in Paris","a story about ...",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")



the_hunger_games = media.Movie("The Hunger Games","a story about a ...",
                               "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=3PkkHsuMrho")


movies = [toy_story,avavtar,logan,ratatouille,midnight_in_paris,the_hunger_games]
#fresh_tomatoes.open_movies_page(movies)


print avavtar.valid_ratings
print media.Movie.valid_ratings
print media.Movie.__doc__
print media.Movie.__module__

