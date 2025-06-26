import re

def extract_text_from_vtt(vtt_file_path, output_file_path):
    with open(vtt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize an empty list to hold the text
    text_lines = []

    # Regular expression patterns to match UUIDs and timestamps
    uuid_pattern = re.compile(r'^[0-9a-fA-F-]{36}-[0-9]$')
    timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}$')

    # Iterate through each line in the VTT file
    for line in lines:
        stripped_line = line.strip()
        # Check if the line is not empty and does not match UUID or timestamp patterns
        if stripped_line and not uuid_pattern.match(stripped_line) and not timestamp_pattern.match(stripped_line):
            text_lines.append(stripped_line)

    # Join the lines into a single paragraph
    full_text = '\n'.join(text_lines)

    # Write the extracted text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(full_text)

# Example usage
vtt_file_path = 'input.vtt'  # Replace with your VTT file path
output_file_path = 'output.txt'  # Replace with your desired output file path
extract_text_from_vtt(vtt_file_path, output_file_path)
