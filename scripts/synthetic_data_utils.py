import requests
import json
import pandas as pd

def generate_synthetic_data_prompt(start_date, end_date):
    prompt = f"""
Create a synthetic dataset for a household's supermarket expenses over the course of one month, with around 20 rows. The dataset should include the following columns, and the data should be structured as a list of dictionaries (each dictionary representing one row):
- **Date**: Random dates within the month ({start_date} to {end_date}). The date should be in the format YYYY-MM-DD. The client does not make purchases on all of the dates provided.
- **Product**: A list of specific supermarket products (e.g Mineral Water, Organic Mangos, Caramel Cookies, etc.). The products provided should differ from those listed in this prompt.
- **Quantity**: A random number of units purchased (e.g., 1, 2, 3, etc.).
- **Price per unit**: A random price (e.g., between 1 and 10 currency units), with prices that make sense depending on the category (e.g., fruits and vegetables should be cheaper than meat or dairy).
- **Total Cost**: The total cost for that item (Quantity * Price per unit).
- **Category**: A category for each product (e.g., Dairy, Fruits, Vegetables, Meat, Snacks, Bakery, Beverages, Fish etc.). The chosen category should be appropriate and relevant to the product.
- **Payment Method**: Randomly assign whether the payment was made by card, cash, or digital wallet. Increase the frequency of one purchase method over the others.
## Instructions
- Ensure the data is structured always as a list of dictionaries, where each dictionary represents a row, with keys corresponding to the column names. The dataset should be realistic, with the prices and quantities varying according to typical household spending patterns. The dataset should contain 20 rows in total.
- Provide the data directly, avoiding Python code.  
- Ensure the list includes a diverse range of products.  
- Return only the Python list as output, with no additional explanations or text.  
- Ensure that each execution of the prompt provides a different set of products, ensuring unique and varied output. 
- Provide only the data without including quotes such as ```python ``` or ```json ```
## Output Example
Please structure the data in the following JSON format as a list of dictionaries:
[
    {{"Date": "{start_date}", "Product": "Whole Milk", "Quantity": 2, "Price per unit": 1.5, "Total Cost": 3.0, "Category": "Dairy", "Payment Method": "Card"}},
    {{"Date": "{start_date}", "Product": "Whole Wheat Bread", "Quantity": 1, "Price per unit": 2.0, "Total Cost": 2.0, "Category": "Bakery", "Payment Method": "Cash"}},
    {{"Date": "{start_date}", "Product": "Organic Bananas", "Quantity": 5, "Price per unit": 0.8, "Total Cost": 4.0, "Category": "Produce", "Payment Method": "Digital Wallet"}},
    ...
]
"""
    return prompt

def generate_synthetic_data(prompt, agent, model, headers):
    # Prepare the data for the API request
    data = {
        "model": model,
        "messages": [{"role": "system", "content": agent},
                     {"role": "user", "content": prompt}]
    }
    
    # Send the API request
    url = "https://api.mistral.ai/v1/chat/completions"
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the response is successful
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()
        content = response_json['choices'][0]['message']['content']
        # Return the content
        return content
    else:
        return None

def convert_api_response_to_dataframe(api_response):
    """
    Converts the API response (in JSON format) into a Pandas DataFrame.
    
    Parameters:
    api_response (str): The API response in JSON format (string).
    
    Returns:
    pd.DataFrame: A DataFrame containing the data from the API response.
    """
    # Parse the JSON string into a Python list
    data = json.loads(api_response)
    
    # Convert the list of dictionaries into a Pandas DataFrame
    df = pd.DataFrame(data)
    
    return df