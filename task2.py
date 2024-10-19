#Identify the city with the highest number of restaurants in the dataset.

import pandas as pd
# Load the dataset
df = pd.read_excel('Dataset cognifyz task b.xlsx', sheet_name='Dataset ')
#count the number of restaurants in each city
city_restaurant_count = df.groupby('City')['Restaurant ID'].count()
# Sort the result in descending order to get the city with the most restaurants
city_restaurant_count_sorted = city_restaurant_count.sort_values(ascending=False)
# Display the city with the highest number of restaurants
top_city = city_restaurant_count_sorted.head(1)
print(f"The city with the highest number of restaurants is {top_city.index[0]} with {top_city.values[0]} restaurants.")
