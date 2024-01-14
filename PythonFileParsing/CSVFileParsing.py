import csv

csv_file_path = "/CYANCONNODE/Data.csv"


def parse_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Process rows as needed
        for row in csv_reader:
            # Your parsing logic for CSV file goes here
            print(f'{row}')


# parse_csv_file(csv_file_path)

if __name__ == "__main__":
    text_file_path = 'Textfile.txt'
    parse_csv_file(text_file_path)

