import re
import csv
import os

def process_logs(input_file, output_file):
    """
    Reads a log file, extracts numerical values following 'TEMP:',
    and saves them to a CSV file.
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    data_to_write = []

    # Regex to find TEMP: followed by optional space and a number (int or float)
    pattern = re.compile(r'TEMP:\s*([\d\.]+)')

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            match = pattern.search(line)
            if match:
                data_to_write.append([match.group(1)])

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # Adding a header as is standard for CSVs
        writer.writerow(['Temperature'])
        writer.writerows(data_to_write)

    print(f"Successfully processed {len(data_to_write)} records to {output_file}")

if __name__ == "__main__":
    process_logs('logs.txt', 'clean_data.csv')
