import pandas as pd
from collections import Counter

# Function to clean and split cuisine combinations
def get_sorted_combinations(cuisines):
    if pd.isna(cuisines):  # Check for nun (missing) values
        return tuple()  
    # Clean the data means remove extra spaces, split by comma, and sort
    cuisine_list = [c.strip() for c in cuisines.split(',')]
    cuisine_list.sort()  # Sort alphabetically and combinations
    return tuple(cuisine_list)

# Load the Excel file
df = pd.read_excel('Level 2.xlsx')

# Apply the function to the 'Cuisines' column to get sorted combinations
df['Cuisine_Combinations'] = df['Cuisines'].apply(get_sorted_combinations)

# Count each combination
combination_counts = Counter(df['Cuisine_Combinations'])

# Get the most common combinations, sorted by frequency
most_common_combinations = combination_counts.most_common()

# Print results, ordered by the most common combinations
print("Most Common Cuisine Combinations:")
for combo, count in most_common_combinations:
    if combo: 
        print(f"{combo}: {count} times")
