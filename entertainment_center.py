import media
import fresh_tomatoes

#Define instances of Class Movie() inside media.py 
toy_story = media.Movie("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy\'s favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he\'s a real spaceman on a mission to return to his home planet.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na\'vi, beings who appear primitive but are highly evolved. Because the planet\'s environment is poisonous, human/N\a'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora.",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

punisher = media.Movie("The Punisher",
                     "This dark action film, based on the comic book series, follows FBI agent Frank Castle (Thomas Jane) as he transforms into the vengeful Punisher after criminals murder his family, including his wife and son.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Punisher_ver2.jpg/220px-Punisher_ver2.jpg",
                     "https://youtu.be/G59cD1NSbS8")

finding_nemo = media.Movie("Finding Nemo",
                     "Marlin (Albert Brooks), a clown fish, is overly cautious with his son, Nemo (Alexander Gould), who has a foreshortened fin. When Nemo swims too close to the surface to prove himself, he is caught by a diver, and horrified Marlin must set out to find him.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",
                     "https://youtu.be/KFu_26DrLE4")

despicable_me = media.Movie("Despicable Me",
                     "A man who delights in all things wicked, supervillain Gru (Steve Carell) hatches a plan to steal the moon. Surrounded by an army of little yellow minions and his impenetrable arsenal of weapons and war machines, Gru makes ready to vanquish all who stand in his way.",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcStk75A_FacVc2kXVb8vdTAU6x-fmRjV2X0-6yxHF5iksQmzKwB",
                     "https://youtu.be/sUkZFetWYY0")

over_the_hedge = media.Movie("Over the Hedge",
                     "When Verne (Garry Shandling) and fellow woodland friends awake from winter\'s hibernation, they find they have some new neighbors: humans, and RJ (Bruce Willis), an opportunistic raccoon who shows the others how to exploit the suburban bounty laid out before them.",
                     "http://www.gstatic.com/tv/thumb/movieposters/159725/p159725_p_v8_aa.jpg",
                     "https://youtu.be/BE77igZczlI")

#create list of all movie instances
movies = [toy_story, avatar,punisher,finding_nemo, despicable_me,over_the_hedge]
#send list to the open_movies_page page function to generate HTML file.
fresh_tomatoes.open_movies_page(movies)


