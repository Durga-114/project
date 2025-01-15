import sqlite3
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

conn = sqlite3.connect('guest_management.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS Amenities (
    amenity_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS Interactions (
    interaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amenity_id INTEGER,
    interaction_type TEXT, -- e.g., "view", "book", "like"
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (amenity_id) REFERENCES Amenities(amenity_id)
);
''')

conn.commit()
def calculate_hybrid_recommendations(user_id):
    
    query = '''
    SELECT user_id, amenity_id, COUNT(*) AS interaction_count
    FROM Interactions
    GROUP BY user_id, amenity_id
    '''
    df = pd.read_sql_query(query, conn)

   
    user_item_matrix = df.pivot(index='user_id', columns='amenity_id', values='interaction_count').fillna(0)

    user_similarity_matrix = cosine_similarity(user_item_matrix)
    user_index = list(user_item_matrix.index).index(user_id)

    similar_users = user_similarity_matrix[user_index]

    recommendations = user_item_matrix.T.dot(similar_users)
    recommendations = pd.Series(recommendations, index=user_item_matrix.columns).sort_values(ascending=False)

    return recommendations.index.tolist()
def add_new_interaction(user_id, amenity_id, interaction_type):
   
    cursor.execute('''
    INSERT INTO Interactions (user_id, amenity_id, interaction_type)
    VALUES (?, ?, ?)
    ''', (user_id, amenity_id, interaction_type))
    conn.commit()

    updated_recommendations = calculate_hybrid_recommendations(user_id)
    print(f"Updated recommendations for User {user_id}: {updated_recommendations}")
def get_user_profile(user_id):
    query = '''
    SELECT a.name, i.interaction_type, COUNT(*) as count
    FROM Interactions i
    JOIN Amenities a ON i.amenity_id = a.amenity_id
    WHERE i.user_id = ?
    GROUP BY a.name, i.interaction_type
    '''
    profile = pd.read_sql_query(query, conn, params=(user_id,))
    return profile

cursor.execute('INSERT OR IGNORE INTO Users (user_id, name) VALUES (?, ?)', (1, 'Alice'))
cursor.execute('INSERT OR IGNORE INTO Users (user_id, name) VALUES (?, ?)', (2, 'Bob'))

cursor.execute('INSERT OR IGNORE INTO Amenities (amenity_id, name, category) VALUES (?, ?, ?)', (101, 'Spa', 'Wellness'))
cursor.execute('INSERT OR IGNORE INTO Amenities (amenity_id, name, category) VALUES (?, ?, ?)', (102, 'Fine Dining', 'Food'))
cursor.execute('INSERT OR IGNORE INTO Amenities (amenity_id, name, category) VALUES (?, ?, ?)', (103, 'Yoga Class', 'Fitness'))
conn.commit()

add_new_interaction(1, 101, "view")
add_new_interaction(1, 102, "book")
add_new_interaction(2, 101, "view")

recommendations = calculate_hybrid_recommendations(1)
print(f"Recommended amenities for User 1: {recommendations}")

user_profile = get_user_profile(1)
print("User Profile:")
print(user_profile)
