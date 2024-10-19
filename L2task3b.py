import pandas as pd
df = pd.read_excel('Level 2.xlsx')
df.head()
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Extract latitude and longitude
coords = df[['Latitude', 'Longitude']]

# K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(coords)

# Plot the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Longitude', y='Latitude', hue='Cluster', palette='viridis')
plt.title('Restaurant Clusters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
import folium
from folium.plugins import HeatMap

# Create a base map
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Prepare data for heatmap
heat_data = df[['Latitude', 'Longitude']].values

# Add heatmap layer to the map
HeatMap(heat_data).add_to(restaurant_map)

# Save and display the map
restaurant_map.save('restaurant_heatmap.html')
