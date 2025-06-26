def remove_timestamps(vtt_file_path, output_file_path):
    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
        lines = vtt_file.readlines()

    # Initialize an empty list to hold the text content
    text_content = []

    for line in lines:
        # Skip lines that contain timestamps or are empty
        if '-->' in line or line.strip() == '':
            continue
        # Add the line to the text content, stripping whitespace
        text_content.append(line.strip())

    # Join the text content into a single paragraph
    paragraph = '\n'.join(text_content)

    # Write the output to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(paragraph)

# Example usage
vtt_file_path = 'input.vtt'  # Replace with your input VTT file path
output_file_path = 'output.txt'  # Replace with your desired output file path
remove_timestamps(vtt_file_path, output_file_path)