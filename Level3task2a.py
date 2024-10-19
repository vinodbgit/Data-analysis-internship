import pandas as pd

# Load the dataset 
df = pd.read_excel('Level 2.xlsx')

# Step 2: Find the restaurant with the highest and lowest number of votes
highest_votes_restaurant = df.loc[df['Votes'].idxmax()]
lowest_votes_restaurant = df.loc[df['Votes'].idxmin()]

# Step 3: Display the results
print("Restaurant with the Highest Number of Votes:")
print(f"Restaurant Name: {highest_votes_restaurant['Restaurant Name']}")
print(f"Votes: {highest_votes_restaurant['Votes']}")
print(f"Location: {highest_votes_restaurant['City']}")

print("\nRestaurant with the Lowest Number of Votes:")
print(f"Restaurant Name: {lowest_votes_restaurant['Restaurant Name']}")
print(f"Votes: {lowest_votes_restaurant['Votes']}")
print(f"Location: {lowest_votes_restaurant['City']}")
