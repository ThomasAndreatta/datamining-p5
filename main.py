#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/mood_dataset.csv')

def filter(id, variable):
    tmp=df
    if(id):
        tmp = tmp[tmp['id'] == id]
    if(variable):
        tmp = tmp[tmp['variable'] == variable]
    return tmp


tmp=filter('AS14.01','mood')
tmp['time'] = pd.to_datetime(df['time'])
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1: Line plot of mood over time
axs[0, 0].plot(tmp['time'], tmp['value'], marker='o', color='blue')
axs[0, 0].set_title('Mood over Time')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Mood Value')
axs[0, 0].grid(True)
axs[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Bar plot of mood values
axs[0, 1].bar(tmp['id'], tmp['value'], color='green')
axs[0, 1].set_title('Mood Values')
axs[0, 1].set_xlabel('ID')
axs[0, 1].set_ylabel('Mood Value')
axs[0, 1].grid(True)

# Plot 3: Histogram of mood values
axs[1, 0].hist(tmp['value'], bins=3, color='purple')
axs[1, 0].set_title('Mood Distribution')
axs[1, 0].set_xlabel('Mood Value')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].grid(True)

# Plot 4: Pie chart of mood distribution
mood_counts = tmp['value'].value_counts()
axs[1, 1].pie(mood_counts, labels=mood_counts.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral'])
axs[1, 1].set_title('Mood Distribution')
axs[1, 1].axis('equal')

# Adjust layout and display plots
plt.tight_layout()
plt.show()

