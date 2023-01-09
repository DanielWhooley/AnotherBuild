import csv


def storedata(data):
    with open("malicious_hashes.csv", "w", newline="") as x:
        writer = csv.writer(x)
        # Write the header row
        writer.writerow(["family", "imphash", "rich_hash"])
        # Write the data rows
        for row in data:
            writer.writerow(row)
