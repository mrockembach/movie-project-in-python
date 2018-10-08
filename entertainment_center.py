import fresh_tomatoes
import media

# These are the favorite movies included in the code.
# You can modify this data, this will update the html file
return_of_the_jedi = media.Movie(
    "Star Wars: Return of the Jedi",
    "After a daring mission to rescue Han Solo from Jabba the Hutt,\
    the rebels dispatch to Endor to destroy a more powerful Death Star.",
    "http://www.impawards.com/1983/posters/return_of_the_jedi_ver1.jpg",
    "https://www.youtube.com/watch?v=3m0rUHvS9pg")

the_empire_strikes_back = media.Movie(
    "Star Wars: The Empire Strikes Back",
    "Luke Skywalker begins Jedi training with Yoda, while his friends \
    are pursued by Darth Vader",
    "http://www.impawards.com/1980/posters/empire_strikes_back_ver3.jpg",
    "https://www.youtube.com/watch?v=xESiohGGP7g")

school_of_rock = media.Movie(
    "School of Rock",
    "After being kicked out of a rock band, Dewey Finn becomes a \
    substitute teacher of a strict elementary private school, only \
    to try and turn it into a rock band",
    "http://www.impawards.com/2003/posters/school_of_rock_ver2.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

into_the_wild = media.Movie(
    "Into the Wild",
    "After graduating from Emory University, top student and athlete \
    Christopher McCandless abandons his possessions. Along the way, \
    Christopher encounters a series of characters that shape his life",
    "http://www.impawards.com/2007/posters/into_the_wild.jpg",
    "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

captain_fantastic = media.Movie(
    "Captain Fantastic",
    "In the forests of the Pacific Northwest, a father devoted to \
    raising his six kids with a rigorous physical and intellectual \
    education is forced to leave his paradise and enter the world, \
    challenging his idea of what it means to be a parent",
    "http://www.impawards.com/2016/posters/captain_fantastic_xlg.jpg",
    "https://www.youtube.com/watch?v=D1kH4OMIOMc")

the_return_of_the_king = media.Movie(
    "Lord of the Ring: the Return of the King",
    "Gandalf and Aragorn lead the World of Men against Sauron's \
    army to draw his gaze from Frodo and Sam as they approach \
    Mount Doom with the One Ring",
    "http://www.impawards.com/2003/posters/lord_of_the_rings_the_return_of_the_king_ver3.jpg",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")


movies = [return_of_the_jedi, the_empire_strikes_back, school_of_rock,
          into_the_wild, captain_fantastic, the_return_of_the_king]
fresh_tomatoes.open_movies_page(movies)
