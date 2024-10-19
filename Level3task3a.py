import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('Level 2.xlsx')

# Step 1: Extract the columns and clean the data
df = df[['Price range', 'Has Online delivery', 'Has Table booking']].dropna()

# Step 2: Convert 'Yes' and 'No' to 1 and 0 for analysis
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})

# Step 3: Group by 'Price range' 
# calculate the percentage of restaurants offering delivery and table booking
price_range_online_delivery = df.groupby('Price range')['Has Online delivery'].mean() * 100
price_range_table_booking = df.groupby('Price range')['Has Table booking'].mean() * 100

# Step 4: Display the results
print("Percentage of Restaurants Offering Online Delivery by Price Range:")
print(price_range_online_delivery)

print("\nPercentage of Restaurants Offering Table Booking by Price Range:")
print(price_range_table_booking)

# Step 5: Visualize the relationship using bar plots
plt.figure(figsize=(12, 5))

# Plot for online delivery
plt.subplot(1, 2, 1)
price_range_online_delivery.plot(kind='bar', color='blue')
plt.title('Percentage of Restaurants Offering Online Delivery by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants')

# Plot for table booking
plt.subplot(1, 2, 2)
price_range_table_booking.plot(kind='bar', color='green')
plt.title('Percentage of Restaurants Offering Table Booking by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants')

plt.tight_layout()
plt.show()
