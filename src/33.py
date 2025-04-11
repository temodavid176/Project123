import numpy as np
import pandas as pd

def load_data():
    # Load your data here
    df = pd.DataFrame(np.random.rand(4, 5))
    return df

def analyze_data(data):
    """
    Analyze the data by performing some basic operations.
    
    Parameters:
        - data (pd.DataFrame): The input dataframe containing numerical and categorical data.

    Returns:
        - result: A dictionary with analysis results.
    """
    mean = data.mean()
    median = data.median()
    std_dev = data.std()
    
    # Perform simple calculations
    sum_data = data.sum()
    average = data.mean()
    minimum_value = data.min()
    maximum_value = data.max()
    
    return {
        "mean": mean,
        "median": median,
        "std_dev": std_dev,
        "sum_data": sum_data,
        "average": average,
        "minimum_value": minimum_value,
        "maximum_value": maximum_value
    }

def visualize_data(data, title="Data Analysis", xlabel="X-axis", ylabel="Y-axis"):
    """
    Visualize the data by creating a chart.
    
    Parameters:
        - data (pd.DataFrame): The input dataframe containing numerical and categorical data.
        - title (str): The title of the chart.
        - xlabel (str): The label for the X-axis.
        - ylabel (str): The label for the Y-axis.

    Returns:
        - fig: A matplotlib figure object.
    """
    fig, ax = plt.subplots()
    
    # Plotting
    data.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    return fig

# Example usage
data = load_data()
analysis_result = analyze_data(data)
visualize_data(data, title="Data Analysis", xlabel="X-axis", ylabel="Y-axis")
