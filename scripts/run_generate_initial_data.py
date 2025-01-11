import os
import pandas as pd
from generate_initial_data import generate_initial_data

# Define the agent, model, and headers (update these with your actual values)
agent = 'This is an agent for generating synthetic data.'
# Set the headers for the API request, including the token for authentication
token = os.getenv('MISTRAL_API_KEY', '')
headers = {
    'Authorization': f'Bearer {token}'
}

# Define the model that will be used for generating the synthetic data
model = "mistral-large-2407"  

# Get the path to the 'data' folder, which is at the same level as the 'scripts' folder
project_dir = os.path.dirname(os.path.abspath(__file__)) 
data_folder = os.path.join(project_dir, '..', 'data')   

# Create the 'data' folder if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)


# Generate the initial data
df = generate_initial_data(agent, model, headers)

# Save the DataFrame to a CSV file in the 'data' folder
output_file_path = os.path.join(data_folder, "supermarket_purchases_data.csv")
df.to_csv(output_file_path, index=False)

print(f"Data saved to {output_file_path}")