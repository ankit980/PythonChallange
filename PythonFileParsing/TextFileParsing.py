import csv

text_file_path = "/CYANCONNODE/Textfile.txt"


def parse_text_file(text_file_path):
    data_list = []
    data_dict = {}
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            # Split the line based on the delimiter (comma in this case)
            fields = line.strip().split(', ')

            # Initialize an empty dictionary to store the extracted data

            # Extract data from each field and populate the dictionary
            for field in fields:
                key, value = field.split(': ')
                data_dict[key] = value

            # Append the structured data to the list
            data_list.append(data_dict)

    # return data_list
    return data_dict


if __name__ == "__main__":
    text_file_path = 'Textfile.txt'
    extracted_data = parse_text_file(text_file_path)

    # Print process the extracted data based on key

    key_to_extract = 'Product ID'
    if key_to_extract in extracted_data:
        print(f"{key_to_extract} values: {extracted_data[key_to_extract]}")
    else:
        print(f"No data found for key: {key_to_extract}")

    # For complete data set

    for key, value in extracted_data.items():
        print(f"{key}:{value}")
