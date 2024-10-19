#Calculate the percentage of restaurants that serve each of the top cuisines.

import pandas as pd

# Load the dataset
df = pd.read_excel('Level 2.xlsx')

# Step 1: Extract and clean the 'Cuisines' column
df['Cuisines'] = df['Cuisines'].fillna('')  # Replace missing values with an empty string

# Step 2: Split the cuisines into separate rows
# Explode the 'Cuisines' column (assuming multiple cuisines are separated by commas)
df['Cuisines'] = df['Cuisines'].apply(lambda x: x.split(', '))
cuisines_exploded = df.explode('Cuisines')

# Step 3: Count the occurrences of each cuisine
cuisine_counts = cuisines_exploded['Cuisines'].value_counts()

# Step 4: Calculate the total number of restaurants
total_restaurants = df.shape[0]

# Step 5: Calculate the percentage for each cuisine
cuisine_percentages = (cuisine_counts / total_restaurants) * 100

# Display the top 10 cuisines with their percentages
top_cuisines = cuisine_percentages.head(10)
print("Top 10 Cuisines and the Percentage of Restaurants Serving Them:")
print(top_cuisines)

# Optionally, export the results to a CSV file
top_cuisines.to_csv('Dataset .csv', index=True)
