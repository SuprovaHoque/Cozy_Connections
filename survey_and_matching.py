import pandas as pd

def match_donation_to_families(user_data, dataset_path):
    # Load the dataset
    dataset = pd.read_csv(dataset_path)

    num_items_donated = user_data['num_items_donated']
    demographics = user_data['demographics']
    
    matching_families = 0
    nearest_drop_off_location = ""

    for index, row in dataset.iterrows():
        min_items_needed = row['min. # items needed']
        family_demographics = row['Demographic'].split(', ')

        # Check if the user's donation can benefit the family
        if num_items_donated >= min_items_needed:
            # Check if all selected demographics are present in the family demographics
            if all(demo in family_demographics for demo in demographics):
                matching_families += 1
                num_items_donated -= min_items_needed

    # Determine the nearest drop-off location based on user's region
    user_region = user_data['region'].lower()
    if user_region == 'north east':
        nearest_drop_off_location = "North East Drop-Off Center"
    elif user_region == 'north west':
        nearest_drop_off_location = "North West Drop-Off Center"
    elif user_region == 'south east':
        nearest_drop_off_location = "South East Drop-Off Center"
    elif user_region == 'south west':
        nearest_drop_off_location = "South West Drop-Off Center"

    return matching_families, nearest_drop_off_location

# Example usage:
user_data = {
    'region': 'north east',  # User's selected region
    'num_items_donated': 15,  # The number of items the user is donating
    'demographics': ['female adult', 'male adult', 'male child', 'male infant'],  # User-selected demographics
}

dataset_path = 'C:\\Users\\sara2\\Desktop\\hack_the_change\\refugee_data2.csv'

matching_families, nearest_location = match_donation_to_families(user_data, dataset_path)

if matching_families > 0:
    print(f"{matching_families} familie(s) will benefit from your donation.")
    print(f"The nearest drop-off location for you is at: {nearest_location}.")
else:
    print("No matching families found for your donation.")