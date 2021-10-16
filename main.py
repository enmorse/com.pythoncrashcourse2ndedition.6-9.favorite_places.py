# Make a dictionary named favorite_places.
# Think of three names to use as keys in the
# dictionary, and store one to three favorite
# places for each person. To make this exercise
# a bit more interesting, ask some friends to name
# a few of their favorite places. Loop through the
# dictionary, and print each person's name and
# their favorite places.
favorite_places = {
    "ernest": {
        "d&d world": "dragonlance",
    },
    "nate": {
       "d&d world": "ravenloft",
    },
    "vincent": {
       "d&d world": "faerun",
    },
}

for key, value in favorite_places.items():
    print(f"\nName: {key.title()}")
    print(f"Favorite D&D World: {value}")
