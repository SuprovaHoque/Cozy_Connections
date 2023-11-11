import pandas as pd

# Load the Excel file into a DataFrame
file_path = r'C:\Users\sara2\Desktop\hack_the_change'
df = pd.read_excel('file_path', engine='openpyxl')


def match_donation_to_families(donation, dataset):
    closest_match = None
    min_difference = float('inf')

    for index, row in dataset.iterrows():
        family_id = row['Family ID']
        # Extract age demographics from the dataset
        age_demographics = row[['infants', 'toddlers', 'children', 'tweens', 'teens', 'adults']]
        
        # Calculate the difference between the donation and the family's age demographics
        difference = sum(abs(donation[age_group] - age_demographics[age_group]) for age_group in donation)

        if difference < min_difference:
            closest_match = family_id
            min_difference = difference

    return closest_match

# Collect user input for the donation
donation = {
    'infants': int(input("Enter the number of items for infants: ")),
    'toddlers': int(input("Enter the number of items for toddlers: ")),
    'children': int(input("Enter the number of items for children: ")),
    'tweens': int(input("Enter the number of items for tweens: ")),
    'teens': int(input("Enter the number of items for teens: ")),
    'adults': int(input("Enter the number of items for adults: ")),
}

# Call the matching function
closest_match = match_donation_to_families(donation, df)

# Display the closest matching family ID
if closest_match is not None:
    print("Closest matching family ID:", closest_match)
else:
    print("No matching families found.")
