import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'hessi.solar.flare.2002to2016.csv'
solar_flare_data = pd.read_csv(file_path)

# Convert date columns for time series analysis
solar_flare_data['start.date'] = pd.to_datetime(solar_flare_data['start.date'])

# Summary statistics
print('Data Summary:')
print(solar_flare_data.describe(include='all'))

# Set up subplots for visualizations
plt.figure(figsize=(10, 7))

# Plot 1: Number of flares per year
plt.subplot(2, 2, 1)
solar_flare_data['start.date'].dt.year.value_counts().sort_index().plot(kind='bar', color='orange')
plt.title('Number of Solar Flares per Year')
plt.xlabel('Year')
plt.ylabel('Number of Flares')

# Plot 2: Distribution of flare durations
plt.subplot(2, 2, 2)
sns.histplot(solar_flare_data['duration.s'], bins=50, kde=True, color='blue')
plt.title('Distribution of Flare Durations (seconds)')
plt.xlabel('Duration (s)')
plt.ylabel('Frequency')

# Plot 3: Energy range distribution
plt.subplot(2, 2, 3)
solar_flare_data['energy.kev'].value_counts().sort_index().plot(kind='bar', color='purple')
plt.title('Distribution of Energy Ranges (keV)')
plt.xlabel('Energy Range (keV)')
plt.ylabel('Number of Flares')


# Plot 4: Correlation heatmap
plt.subplot(2, 2, 4)
correlation = solar_flare_data[['duration.s', 'peak.c/s', 'total.counts', 'x.pos.asec', 'y.pos.asec', 'radial']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.show()

