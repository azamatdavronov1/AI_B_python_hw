import requests
import random

API_KEY = "couldNotTookThatAPI"  # Replace with your actual API key
BASE_URL = "https://api.themoviedb.org/3"

print("Movie Recommendation System")
genre_name = input("Enter a movie genre: ").strip().lower()

# Fetch available genres
genres = requests.get(f"{BASE_URL}/genre/movie/list?api_key={API_KEY}").json().get("genres", [])
genre_dict = {g["name"].lower(): g["id"] for g in genres}

if genre_name in genre_dict:
    genre_id = genre_dict[genre_name]
    movies = requests.get(f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}").json().get("results", [])

    if movies:
        movie = random.choice(movies)
        print(f"Recommended Movie: {movie['title']}")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found for this genre. Try another one.")
else:
    print("Invalid genre. Please enter a valid genre name.")

