import pandas as pd
import json
import os
from synthetic_data_utils import generate_synthetic_data_prompt, generate_synthetic_data

def update_product_csv_with_new_week_data(csv_file, start_date, end_date, agent, model, headers):
    """
    Update the CSV file with new synthetic data for a specific week.
    Args:
        csv_file (str): Name of the CSV file to update (located in the 'data' folder).
        start_date (str): The start date of the week (format: 'YYYY-MM-DD').
        end_date (str): The end date of the week (format: 'YYYY-MM-DD').
        agent: The agent to interact with the API.
        model: The model configuration for the API.
        headers: The headers required for the API request.
    Returns:
        pd.DataFrame: The combined DataFrame with the new week data added.
    """
    # Define the relative path to the 'data' folder from the 'scripts' folder
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the script's directory
    data_folder = os.path.join(script_dir, '..', 'data')  # Navigate to the data folder
    
    # Construct the full path to the CSV file in the data folder
    csv_path = os.path.join(data_folder, csv_file)

    # Read the existing data from the CSV file
    df_existing = pd.read_csv(csv_path)

    # Generate data for the specified week
    prompt = generate_synthetic_data_prompt(start_date, end_date)
    response_api = generate_synthetic_data(prompt, agent, model, headers)
    
    # Parse the new week data into a list of dictionaries
    data_new_week = json.loads(response_api)
    
    # Convert the new data into a DataFrame
    df_new_week = pd.DataFrame(data_new_week)
    
    # Combine the existing data with the new data
    df_combined = pd.concat([df_existing, df_new_week], ignore_index=True)
    
    # Save the updated data back to the CSV
    df_combined.to_csv(csv_path, index=False)
    
    return df_combined