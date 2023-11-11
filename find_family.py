import pandas as pd

# Load the dataset (replace 'your_dataset.xlsx' with the actual file path)
dataset_path = r'your_dataset.xlsx'
df = pd.read_excel(dataset_path, engine='openpyxl')

def match_donation_to_families(user_data, dataset):
    num_items_donated = user_data['num_items_donated']
    demographics = user_data['demographics']
    
    matching_families = []

    for index, row in dataset.iterrows():
        num_people = row['Number of People']
        num_females = sum(int(x.split(' ')[-1]) for x in row['# of Females'].split(', '))
        num_males = sum(int(x.split(' ')[-1]) for x in row['# of Males'].split(', '))
        total_clothes_needed = num_females + num_males

        if num_items_donated >= total_clothes_needed:
            matching_families.append(row['Family ID Number'])
            num_items_donated -= total_clothes_needed

    return matching_families

def find_nearest_drop_off_location(user_address):
    # Implement logic to find the nearest drop-off location based on user's address
    # Replace this placeholder logic with a real implementation
    nearest_location = "123 Main St, City, State"
    return nearest_location

def main():
    print("Welcome to our donation platform!")
    print("Please fill out the survey to make a difference.")
    
    user_address = input("Where do you live? (Address): ")
    num_items_donated = int(input("How many items are you donating? (10 to 40+): "))
    
    print("Select gender and age demographics that apply to your donation:")
    print("1. Male")
    print("2. Female")
    print("3. Children (Age < 18)")
    print("4. Adults (Age 18-64)")
    print("5. Seniors (Age 65+)")
    
    demographics = []
    while True:
        choice = input("Enter the number of the demographic you want to select (or 'done' to finish): ")
        if choice == 'done':
            break
        demographics.append(choice)
    
    user_data = {
        'user_address': user_address,
        'num_items_donated': num_items_donated,
        'demographics': demographics,
    }
    
    matching_families = match_donation_to_families(user_data, df)
    
    if matching_families:
        nearest_location = find_nearest_drop_off_location(user_address)
        print(f"Thank you for your donation! {len(matching_families)} families will benefit from your generosity.")
        print(f"The nearest drop-off location for you is at: {nearest_location}.")
    else:
        print("We couldn't find matching families for your donation. Please consider donating to a different cause.")

if __name__ == "__main__":
    main()