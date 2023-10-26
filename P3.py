import numpy as np

# Sample user-movie ratings data
# Rows represent users, columns represent movies, and values represent ratings (0-5)
ratings = np.array([
    [5, 4, 0, 0, 1],
    [4, 5, 3, 0, 0],
    [0, 1, 0, 5, 4],
    [2, 0, 0, 4, 5]
])

# Function to calculate recommendations for a user
def recommend_movies(user_id, ratings, num_recommendations):
    # Calculate the similarity between the user and all other users
    user_ratings = ratings[user_id]
    similarities = np.dot(ratings, user_ratings) / (np.linalg.norm(ratings, axis=1) * np.linalg.norm(user_ratings))

    # Sort the users by similarity in descending order
    similar_users = np.argsort(similarities)[::-1]

    # Find movies that the user has not rated but the most similar user has
    recommendations = []
    for movie_id in range(ratings.shape[1]):
        if user_ratings[movie_id] == 0:
            for user in similar_users:
                if ratings[user][movie_id] > 0:
                    recommendations.append(movie_id)
                    break

        if len(recommendations) >= num_recommendations:
            break

    return recommendations

# User ID (0-based index) for whom you want to make recommendations
user_id = 0

# Number of movie recommendations to provide
num_recommendations = 3

recommended_movies = recommend_movies(user_id, ratings, num_recommendations)

print(f"Recommended movies for User {user_id}:")
for movie_id in recommended_movies:
    print(f"Movie {movie_id}")
