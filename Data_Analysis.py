"""
Life Expectancy Data Analysis

This program analyzes life expectancy data from various countries. It allows the user to explore the data in different ways,
including finding the year and country with the highest and lowest life expectancy, computing the average life expectancy
for a specific year, and finding the min and max life expectancies for a given year.

"""
# Load the dataset from a file
data = []
with open("life-expectancy.csv", 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

# Handle the first line (header)
header = data[0]
data = data[1:]

# Find the highest and lowest life expectancies and their associated year and country
highest_expectancy = float("-inf")
lowest_expectancy = float("inf")
highest_year = ""
highest_country = ""
lowest_year = ""
lowest_country = ""

for i in range(1, len(data)):
    expectancy = float(data[i][3])
    if expectancy > highest_expectancy:
        highest_expectancy = expectancy
        highest_year = data[i][1]
        highest_country = data[i][2]
    if expectancy < lowest_expectancy:
        lowest_expectancy = expectancy
        lowest_year = data[i][1]
        lowest_country = data[i][2]

# Identify the year and country with the largest drop from one year to the next
largest_drop = 0
drop_year = ""
drop_country = ""
for i in range(1, len(data)):
    current_expectancy = float(data[i][3])
    previous_expectancy = float(data[i - 1][3])
    drop = previous_expectancy - current_expectancy
    if drop > largest_drop:
        largest_drop = drop
        drop_year = data[i][1]
        drop_country = data[i][2]

# Prompt the user for a country and calculate its statistics
country_name = input("Enter a country name: ")
country_data = [row for row in data if row[2] == country_name]
if country_data:
    expectancies = [float(row[3]) for row in country_data]
    min_expectancy = min(expectancies)
    max_expectancy = max(expectancies)
    average_expectancy = sum(expectancies) / len(expectancies)
    print(f"Statistics for {country_name}:")
    print(f"Minimum life expectancy: {min_expectancy:.2f}")
    print(f"Maximum life expectancy: {max_expectancy:.2f}")
    print(f"Average life expectancy: {average_expectancy:.2f}")
else:
    print("No data found for the given country.")

# Display the results
print("\nHighest life expectancy:")
print(f"Year: {highest_year}, Country: {highest_country}, Life Expectancy: {highest_expectancy:.2f}")
print("Lowest life expectancy:")
print(f"Year: {lowest_year}, Country: {lowest_country}, Life Expectancy: {lowest_expectancy:.2f}")
print("Largest drop in life expectancy:")
print(f"Year: {drop_year}, Country: {drop_country}, Largest Drop: {largest_drop:.2f}")
