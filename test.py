import pandas as pd
import json
import matplotlib.pyplot as plt

#Create time-series-results.csv
def create_time_series():
    # Open and load data from scores.json
    with open('scores.json') as f:
        data = json.load(f)

    # Ensure data is accessed from the 'scores' key
    scores_data = data.get('scores', [])
    
    # Check if data is loaded as a list (it should be a list of dictionaries)
    print("Data loaded from JSON:", type(scores_data))  # Check the type of data
    
    # If it's not a list, raise an error
    if not isinstance(scores_data, list):
        raise ValueError("Data from scores.json is not in the expected list format.")
    
    # Sort data by timestamp in ascending order (ensure timestamp is in datetime format)
    scores_data_sorted = sorted(scores_data, key=lambda x: x['timestamp'])

    # Create DataFrame from sorted data
    df = pd.DataFrame(scores_data_sorted)
    
    # Debug: Print a few rows to verify the data
    print("Data to be written to CSV:")
    print(df.head())

    # Save to CSV
    df.to_csv('time-series-results.csv', index=False)
    print("time-series-results.csv created successfully.")

def main():
    create_time_series()

if __name__ == '__main__':
    main()