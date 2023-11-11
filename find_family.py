import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('refugee_data.xlsx', engine='openpyxl')

def find_matching_family(user_donation, dataset):
    # Initialize an empty list to store matching families
    matching_families = []

    # Loop through the dataset and check for matches
    for index, row in dataset.iterrows():
        # Modify the following line to match your dataset's column names
        if user_donation == row['NeededItems']:
            matching_families.append(row['FamilyID'])

    if matching_families:
        return matching_families
    else:
        return "No matching families found."

# Usage example
donation_item = "Clothing"  # Replace with the item the user is donating
matching_families = find_matching_family(donation_item, df)
print(matching_families)