import pandas as pd

# Load the Excel file into a DataFrame
file_path = r'C:\Users\sara2\Desktop\hack_the_change'
df = pd.read_excel('file_path', engine='openpyxl')


def match_donation_to_families(donation, dataset):
    matching_families = []

    for index, row in dataset.iterrows():
        family_id = row['Family ID']
        # Extract age demographics from the dataset
        age_demographics = row[['infants', 'toddlers', 'children', 'tweens', 'teens', 'adults']]

        # Check if the donation matches the age demographics
        for age_group, quantity in donation.items():
            if quantity > 0 and age_demographics[age_group] >= quantity:
                matching_families.append(family_id)
            else:
                # Reset the matching flag if any age group does not match
                matching_families = []

        if matching_families:
            break  # No need to continue checking other families if a match is found

    return matching_families

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
matching_families = match_donation_to_families(donation, df)

# Display the IDs of matching families
if matching_families:
    print("Matching family IDs:", matching_families)
else:
    print("No matching families found.")