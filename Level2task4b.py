import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('Level 2.xlsx')

# Step 1: Group by 'Restaurant Name' and calculate average ratings and total votes
restaurant_chains = df.groupby('Restaurant Name').agg(
    avg_rating=('Aggregate rating', 'mean'),
    total_votes=('Votes', 'sum'),
    num_locations=('Restaurant Name', 'size')
).reset_index()

# Step 2: Filter to include only restaurant chains with more than one location
chains = restaurant_chains[restaurant_chains['num_locations'] > 1]

# Step 3: Sort by popularity (total votes) and rating
popular_chains = chains.sort_values(by='total_votes', ascending=False)
top_rated_chains = chains.sort_values(by='avg_rating', ascending=False)

# Display top 10 most popular and highest-rated chains
print("Top 10 Most Popular Restaurant Chains (by votes):")
print(popular_chains.head(10))

print("\nTop 10 Highest Rated Restaurant Chains:")
print(top_rated_chains.head(10))

# Step 4: Visualization (Optional)

# Plot top 10 most popular restaurant chains
plt.figure(figsize=(10, 6))
popular_chains.head(10).plot(kind='barh', x='Restaurant Name', y='total_votes', legend=False)
plt.xlabel('Total Votes')
plt.title('Top 10 Most Popular Restaurant Chains (by Votes)')
plt.gca().invert_yaxis()  # Invert to show highest on top
plt.tight_layout()
plt.show()

# Plot top 10 highest rated restaurant chains
plt.figure(figsize=(10, 6))
top_rated_chains.head(10).plot(kind='barh', x='Restaurant Name', y='avg_rating', legend=False, color='orange')
plt.xlabel('Average Rating')
plt.title('Top 10 Highest Rated Restaurant Chains')
plt.gca().invert_yaxis()  # Invert to show highest on top
plt.tight_layout()
plt.show()
