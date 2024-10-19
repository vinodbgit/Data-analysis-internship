import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
import string
from collections import Counter
import matplotlib.pyplot as plt

# Download stopwords from nltk 
nltk.download('stopwords')

# Load the dataset
file_path = '/mnt/data/Level 2.xlsx'
df = pd.read_excel('Level 2.xlsx')

# Step 2: Extract 'Rating text' as the text to analyze
text_data = df['Rating text'].dropna()

# Step 3: Clean and Tokenize the text
# Convert to lowercase, remove punctuation and stopwords
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Tokenize the text
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return tokens

# Apply the cleaning function to all text data
cleaned_tokens = text_data.apply(clean_text)

# Flatten the list of token lists into a single list
all_words = [word for tokens in cleaned_tokens for word in tokens]

# Step 4: Define positive and negative word dictionaries
positive_words = ["excellent", "good", "great", "amazing", "perfect", "love", "fantastic", "best", "wonderful", "superb"]
negative_words = ["bad", "poor", "terrible", "awful", "disappointing", "worst", "horrible", "mediocre", "boring"]

# Step 5: Count positive and negative word frequencies
positive_word_counts = Counter([word for word in all_words if word in positive_words])
negative_word_counts = Counter([word for word in all_words if word in negative_words])

# Display top positive and negative words
print("Most Common Positive Keywords:")
print(positive_word_counts.most_common(10))

print("\nMost Common Negative Keywords:")
print(negative_word_counts.most_common(10))

# Step 6: Visualization
# Plot positive keywords
plt.figure(figsize=(8, 4))
plt.bar(*zip(*positive_word_counts.most_common(10)), color='green')
plt.title('Top 10 Positive Keywords')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()

# Plot negative keywords
plt.figure(figsize=(8, 4))
plt.bar(*zip(*negative_word_counts.most_common(10)), color='red')
plt.title('Top 10 Negative Keywords')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()
