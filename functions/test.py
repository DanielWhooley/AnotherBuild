import csv
import os
import pefile


def test(root):
    # Create a dictionary to store the hashes and labels
    hashes = {}

    # Open the CSV file in read mode
    with open('malicious_hashes.csv', 'r') as csvfile:
        # Create a reader to parse the CSV file
        reader = csv.reader(csvfile)

        # Iterate over the rows of the file
        for row in reader:
            # Unpack the data into variables
            file, imphash, rich_hash = row
            # Store the hash and label in the dictionary
            hashes[(imphash, rich_hash)] = file

    # Traverse the test directory
    for root, dirs, files in os.walk(root):
        for file in files:
            # Process only the .exe files
            if file.endswith('.exe'):
                # Parse the PE file
                pe = pefile.PE(os.path.join(root, file))
                # Extract the hashes
                imphash = pe.get_imphash()
                rich_header = pe.parse_rich_header()
                if rich_header is not None:
                    rich_hash = rich_header.get_hash()
                else:
                    rich_hash = ''
                # Check if the hash is in the dictionary
                if (imphash, rich_hash) in hashes:
                    # If there is a match, print the family label and the names of the test sample and the train sample
                    print(f'Match found: {file} is from the same family as {hashes[(imphash, rich_hash)]}')
