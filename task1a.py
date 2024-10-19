#Determine the top three most common cuisines in the dataset.

import pandas as pd
import matplotlib.pyplot as plt
file_path = 'path_to_your_file.xlsx'
df = pd.read_excel('Dataset cognifyz task a.xlsx')
print(df.head())  # View the first 5 rows
print(df.columns)  # Check column names
cuisine_counts = df['Cuisines'].value_counts()
print(cuisine_counts)
top_3_cuisines = cuisine_counts.head(3)
print(top_3_cuisines)
# Using Matplotlib
top_3_cuisines.plot(kind='bar', color='skyblue')
plt.title('Top 3 Most Common Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.show()
