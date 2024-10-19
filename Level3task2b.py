import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('Level 2.xlsx')

# Step 1: Check for missing values in 'Votes' and 'Aggregate rating'
df = df[['Votes', 'Aggregate rating']].dropna()

# Step 2: Calculate correlation between number of votes and rating
correlation = df['Votes'].corr(df['Aggregate rating'])
print(f"Correlation between Votes and Aggregate Rating: {correlation}")

# Step 3: Visualize the relationship using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Votes'], df['Aggregate rating'], alpha=0.5)
plt.title('Correlation between Votes and Aggregate Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate Rating')
plt.show()
