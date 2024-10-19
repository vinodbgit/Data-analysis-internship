import pandas as pd
df = pd.read_excel('Level 2.xlsx')

# Group by 'Restaurant Name' to identify potential chains
chains = df.groupby('Restaurant Name').size().reset_index(name='count')

# Filter to include only restaurant names with more than one occurrence
chains = chains[chains['count'] > 1]

# Display the restaurant chains
print(chains)

# Optionally, export the results to a CSV file for further use
chains.to_csv('Dataset.csv', index=False)

# Visualization
import matplotlib.pyplot as plt

# Plot the top 20 restaurant chains by number of locations
top_chains = chains.sort_values(by='count', ascending=False).head(20)
top_chains.plot(kind='bar', x='Restaurant Name', y='count', legend=False)
plt.xlabel('Restaurant Name')
plt.ylabel('Number of Locations')
plt.title('Top 20 Restaurant Chains by Number of Locations')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
