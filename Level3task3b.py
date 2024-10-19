import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/Level 2.xlsx'
df = pd.read_excel('Level 2.xlsx')

# Step 1: Extract the relevant columns and clean the data
df = df[['Price range', 'Has Online delivery', 'Has Table booking']].dropna()

# Step 2: Convert 'Yes' and 'No' to 1 and 0 for analysis
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})

# Step 3: Analyze the correlation between price range and services
correlation_online_delivery = df['Price range'].corr(df['Has Online delivery'])
correlation_table_booking = df['Price range'].corr(df['Has Table booking'])

# Display correlation results
print(f"Correlation between Price Range and Online Delivery: {correlation_online_delivery}")
print(f"Correlation between Price Range and Table Booking: {correlation_table_booking}")

# Step 4: Visualize the relationship using bar plots
price_range_online_delivery = df.groupby('Price range')['Has Online delivery'].mean() * 100
price_range_table_booking = df.groupby('Price range')['Has Table booking'].mean() * 100

plt.figure(figsize=(12, 5))

# Plot for online delivery
plt.subplot(1, 2, 1)
price_range_online_delivery.plot(kind='bar', color='blue')
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants Offering Online Delivery')

# Plot for table booking
plt.subplot(1, 2, 2)
price_range_table_booking.plot(kind='bar', color='green')
plt.title('Table Booking Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants Offering Table Booking')

plt.tight_layout()
plt.show()
