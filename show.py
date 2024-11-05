
import os
import pandas as pd

import matplotlib.pyplot as plt

def visualize_data(directory, filename):
    file_path = os.path.join(directory, filename)
    df = pd.read_csv(file_path, header=None)
    data = df[0].astype(float)
    labels = df[1]

    plt.figure(figsize=(24, 6))
    plt.plot(data, label='Time Series Data', linewidth=1)
    plt.scatter(df.index[labels == 1], data[labels == 1], color='red', label='Anomaly Points', s=50)
    plt.title(f'Time Series Visualization - {filename}')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def visualize_all_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.out')]

    
    def extract_number(filename):
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else float('inf') 

    files.sort(key=extract_number) 

    for file in files:
        visualize_data(directory, file)
