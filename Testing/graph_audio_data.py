import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your actual CSV file
csv_file_path = 'audio_data.csv'

# Load the CSV file, assuming the first column is the index
df = pd.read_csv(csv_file_path, index_col=0)

# Get the number of channels from the DataFrame
num_channels = df.shape[1]

# Create a figure and subplots
fig, axes = plt.subplots(num_channels, 1, figsize=(10, 20))

# Check if there's only one channel to handle the axes as a non-iterable
if num_channels == 1:
    axes = [axes]

# Loop through each channel
for i in range(num_channels):
    ax = axes[i]
    # Plot the audio data for the channel
    ax.plot(df.iloc[:, i])
    ax.set_title(f'Channel {i+1}')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
