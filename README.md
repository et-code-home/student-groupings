# Team Tango

## Group Formation with Student Preferences

### Import preference data with `preference.py`

This script contains the code to read student pairing preferences from a CSV file and organize them into a dictionary. The CSV file should be structured with each row representing a student's preferences, where the first column is the student's name and the subsequent columns represent their preferences for working with other students. The preferences are represented as numerical values:

- -1 indicates that the student prefers not to work with another student
- 0 indicates no preference
- 1 indicates a preferred partner

### Main program

This program is designed to assist in forming groups of students based on their preferences and aversions for working together. It reads student preferences from the dictionary built by the 'preferences' module and creates groups of a specified size, ensuring that students who wish to avoid each other are not placed in the same group. The program follows a two-step process:

1. **Separating Students with Aversions:**
   The program initially separates students who have indicated that they don't want to work together into different groups. 

2. **Filling Remaining Students:**
   After separating students with aversions, the program fills the remaining group slots by accommodating students who have preferred connections with others. It then fills remaining slots with neutral students while observing group size limits and avoiding already placed students.

## Usage

1. Ensure you have the 'preferences.py' file in the same directory, containing the student preference data.
2. Set the `group_size` variable to the desired group size.
3. Run the program in your Python environment.

## Important Notes

- There is a sample data file, `sample-preference-data.csv` that can be used for testing 
- Please ensure that you have reviewed and adjusted the preferences data to accurately reflect student aversions and preferences before using this program.
- **Disclaimer:** This program is provided as an example and may require further testing and refinement for your specific use case.

## Author

Elissa Thomas
