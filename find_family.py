import pandas as pd

#the find_matching_family function  takes the user's donation item and the DataFrame as paramenters

# Load the Excel file into a DataFrame
file_path = r'C:\Users\sara2\Desktop\hack_the_change'

df = pd.read_excel('file_path', engine='openpyxl')

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
donation_item = get_donations()  # will be funcrions to prompt user to enetr inof about inetsm they are donating
matching_families = find_matching_family(donation_item, df)
print(matching_families)