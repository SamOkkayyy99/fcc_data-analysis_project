import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], alpha=0.5, label = 'Rise in Sea Level')

    # Create first line of best fit
    slope1, intercept1, _, _, _ =  linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = slope1 * x1 + intercept1
    plt.plot(x1, y1, 'r', label = 'Line of Best Fit 1')

    # Create second line of best fit
    slope2, intercept2, _, _, _ = linregress(data[data['Year'] >= 2000]['Year'], data[data['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = slope2 * x2 + intercept2
    plt.plot(x2, y2, 'g', label = 'Line of Best Fit 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)') # really, inches...
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()