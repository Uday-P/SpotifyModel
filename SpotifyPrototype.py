import mesa
import random

# Music library
music_library = [
    ("Song 1", "Artist A", "Pop"),
    ("Song 2", "Artist B", "Rock"),
    ("Song 3", "Artist C", "Jazz"),
    ("Song 4", "Artist D", "Electronic"),
    ("Song 5", "Artist E", "Hip-Hop"),
    ("Song 6", "Artist A", "Pop"),
    ("Song 7", "Artist F", "Rock"),
    ("Song 8", "Artist G", "Jazz"),
    ("Song 9", "Artist H", "Electronic"),
    ("Song 10", "Artist I", "Hip-Hop"),
    ("Song 11", "Artist B", "Rock"),
    ("Song 12", "Artist C", "Jazz"),
    ("Song 13", "Artist D", "Electronic"),
    ("Song 14", "Artist E", "Hip-Hop"),
    ("Song 15", "Artist F", "Pop"),
    ("Song 16", "Artist G", "Rock"),
    ("Song 17", "Artist H", "Jazz"),
    ("Song 18", "Artist I", "Electronic"),
    ("Song 19", "Artist J", "Hip-Hop"),
    ("Song 20", "Artist A", "Pop"),
    ("Song 21", "Artist B", "Rock"),
    ("Song 22", "Artist C", "Jazz"),
    ("Song 23", "Artist D", "Electronic"),
    ("Song 24", "Artist E", "Hip-Hop"),
    ("Song 25", "Artist F", "Pop"),
    ("Song 26", "Artist G", "Rock"),
    ("Song 27", "Artist H", "Jazz"),
    ("Song 28", "Artist I", "Electronic"),
    ("Song 29", "Artist J", "Hip-Hop"),
    ("Song 30", "Artist A", "Pop"),
    ("Song 31", "Artist B", "Rock"),
    ("Song 32", "Artist C", "Jazz"),
    ("Song 33", "Artist D", "Electronic"),
    ("Song 34", "Artist E", "Hip-Hop"),
    ("Song 35", "Artist F", "Pop"),
    ("Song 36", "Artist G", "Rock"),
    ("Song 37", "Artist H", "Jazz"),
    ("Song 38", "Artist I", "Electronic"),
    ("Song 39", "Artist J", "Hip-Hop"),
    ("Song 40", "Artist A", "Pop"), 
    ("Song 41", "Artist K", "Classical"),
    ("Song 42", "Artist L", "Country"),
    ("Song 43", "Artist M", "Reggae"),
    ("Song 44", "Artist N", "Metal"),
    ("Song 45", "Artist O", "Folk"),
    ("Song 46", "Artist P", "Classical"),
    ("Song 47", "Artist Q", "Country"),
    ("Song 48", "Artist R", "Reggae"),
    ("Song 49", "Artist S", "Metal"),
    ("Song 50", "Artist T", "Folk"),
    ("Song 51", "Artist K", "Classical"),
    ("Song 52", "Artist L", "Country"),
    ("Song 53", "Artist M", "Reggae"),
    ("Song 54", "Artist N", "Metal"),
    ("Song 55", "Artist O", "Folk"),
    ("Song 56", "Artist P", "Classical"),
    ("Song 57", "Artist Q", "Country"),
    ("Song 58", "Artist R", "Reggae"),
    ("Song 59", "Artist S", "Metal"),
    ("Song 60", "Artist T", "Folk")

]

#print("Music library created!")
#print("Number of songs:", len(music_library))



# Separate familiar and unfamiliar songs
familiar_songs = music_library[:20]
unfamiliar_songs = music_library[20:]

# Generate listening histories
def create_listening_history(familiar_percentage):

    familiar_count = int(20 * familiar_percentage)
    unfamiliar_count = 20 - familiar_count

    history = random.sample(familiar_songs, familiar_count)
    history += random.sample(unfamiliar_songs, unfamiliar_count)

    return history


# Baseline: 80% familiar music
baseline_history = create_listening_history(0.80)

# Alternative: 40% familiar music
alternative_history = create_listening_history(0.40)

#print("Baseline familiar songs:", 16)
#print("Alternative familiar songs:", 8)



# Listener agent
class ListenerAgent(mesa.Agent):

    def __init__(self, model, history):
        super().__init__(model)

        self.history = history
        self.recommendations = []

    def generate_recommendations(self):

        history_genres = {song[2] for song in self.history}

        available_songs = [
            song for song in self.model.library
            if song not in self.history
        ]

        similar_songs = [
            song for song in available_songs
            if song[2] in history_genres
        ]

        other_songs = [
            song for song in available_songs
            if song[2] not in history_genres
        ]

        self.random.shuffle(similar_songs)
        self.random.shuffle(other_songs)

        self.recommendations = (
            similar_songs + other_songs
        )[:30]




# Main recommendation model
class RecommendationModel(mesa.Model):

    def __init__(self, history, library):
        super().__init__()

        self.library = library

        # Create a listener agent
        self.listener = ListenerAgent(self, history)

    def generate_recommendations(self):

        # Ask the listener to generate recommendations
        self.listener.generate_recommendations()

        return self.listener.recommendations



# Create both recommendation models
baseline_model = RecommendationModel(baseline_history, music_library)
alternative_model = RecommendationModel(alternative_history, music_library)

# Generate recommendation lists
baseline_recommendations = baseline_model.generate_recommendations()
alternative_recommendations = alternative_model.generate_recommendations()

# Display the number of recommendations
#print("Baseline recommendations:", len(baseline_recommendations))
#print("Alternative recommendations:", len(alternative_recommendations))



# Measure unfamiliar artists and genres
def measure_diversity(history, recommendations):

    history_artists = {song[1] for song in history}
    history_genres = {song[2] for song in history}

    unfamiliar_artists = {
        song[1] for song in recommendations
        if song[1] not in history_artists
    }

    unfamiliar_genres = {
        song[2] for song in recommendations
        if song[2] not in history_genres
    }

    return len(unfamiliar_artists), len(unfamiliar_genres)


# Measure baseline results
baseline_results = measure_diversity(
    baseline_history, baseline_recommendations
)

# Measure alternative results
alternative_results = measure_diversity(
    alternative_history, alternative_recommendations
)

print("Baseline unfamiliar artists:", baseline_results[0])
print("Baseline unfamiliar genres:", baseline_results[1])

print("Alternative unfamiliar artists:", alternative_results[0])
print("Alternative unfamiliar genres:", alternative_results[1])