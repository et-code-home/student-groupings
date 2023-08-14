import csv

# Define the path to the CSV file
csv_file = "sample-preference-data.csv"

# Initialize an empty dictionary to store pairing preferences
pairing_preferences = {}

# Read the CSV file and populate the pairing_preferences dictionary
# Read the CSV file and populate the dictionary
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        key = row[0]
        values = [int(value) for value in row[1:]]
        pairing_preferences[key] = values

# Print the pairing_preferences dictionary
# print(pairing_preferences)