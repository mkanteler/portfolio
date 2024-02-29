import csv
from collections import Counter
from collections import defaultdict
from tabulate import tabulate

# Initialize an empty list to store words from the CSV file
words = []

# Read from the CSV file 'negative.csv'. FIle contains data of text with comments exported from a Customer Satisfaction Survey
with open(r'C:\Users\marie\Desktop\negative.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for col in reader:
        # Split the content of the first column into words
        csv_words = col[0].split(" ")

        # Iterate over each word and add it to the 'words' list
        for i in csv_words:
            words.append(i)

# Initialize an empty list to store counted words
words_counted = []

# Open a new CSV file 'frequency_result_negative.csv' in append mode
with open('frequency_result_negative.csv', 'a+', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Count the occurrences of each word and append to 'words_counted' list
    for i in words:
        x = words.count(i)
        words_counted.append((i, x))

    # Write the list of counted words to the CSV file
    writer.writerow(words_counted)

# Display the frequency table using tabulate
data = words_counted
col_names = ["word", "times appeared"]

# Print the tabulated data
print(tabulate(data, headers=col_names))
