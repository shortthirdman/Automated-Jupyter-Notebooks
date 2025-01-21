import json
import pandas as pd
from synthetic_data_utils import generate_synthetic_data_prompt, generate_synthetic_data

def generate_initial_data(agent, model, headers):
    """
    Generate synthetic data for the first four weeks of January 2024 using an API.
    Args:
        agent: The agent to interact with the API.
        model: The model configuration for the API.
        headers: The headers required for the API request.
    Returns:
        pd.DataFrame: A DataFrame containing the generated data for all four weeks.
    """
    all_data = []

    # Define week ranges
    week_ranges = [
        ("2024-01-01", "2024-01-07"),
        ("2024-01-08", "2024-01-14"),
        ("2024-01-15", "2024-01-21"),
        ("2024-01-22", "2024-01-28"),
    ]

    # Generate data for each week
    for start_date, end_date in week_ranges:
        prompt = generate_synthetic_data_prompt(start_date, end_date)
        response = generate_synthetic_data(prompt, agent, model, headers)
        week_data = json.loads(response)
        all_data.extend(week_data)

    # Convert the list of data into a DataFrame
    df = pd.DataFrame(all_data)

    return df