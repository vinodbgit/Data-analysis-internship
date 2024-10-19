import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('Level 2.xlsx')

# Step 1: calculate the length of each review in words
# Here we substitute 'Rating text' as reviews, but replace 'Rating text' with actual review column if available
df['review_length'] = df['Rating text'].apply(lambda x: len(str(x).split()))

# Step 2: Calculate the average review length
average_review_length = df['review_length'].mean()
print(f"Average Review Length (in words): {average_review_length}")

# Step 3: the relationship between review length and rating
# Assuming there is a numerical 'Aggregate rating' column
plt.figure(figsize=(10, 6))
plt.scatter(df['review_length'], df['Aggregate rating'], alpha=0.5)
plt.title('Review Length vs. Rating')
plt.xlabel('Review Length (in words)')
plt.ylabel('Aggregate Rating')
plt.show()

# Step 4: Calculate correlation between review length and rating
correlation = df['review_length'].corr(df['Aggregate rating'])
print(f"Correlation between Review Length and Rating: {correlation}")
