import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df.dropna()


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,6))
    df.plot(ax=ax)
    plt.title('Line Plot')
    plt.xlabel('Date')
    plt.ylabel('Values')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10,6))
    df_bar.plot(kind='bar', ax=ax)
    plt.title('Monthly Bar Plot')
    plt.xlabel('Month')
    plt.ylabel('Means')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(x='year', y='value', data=df_box, ax=ax)
    plt.title('Box Plot')
    plt.xlabel('Year')
    plt.ylabel('Values')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
