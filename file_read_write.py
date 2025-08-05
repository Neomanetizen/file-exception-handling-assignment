def modify_content(line):
    # Example modification: convert to uppercase and add line number
    return f"{line_number}: {line.upper()}"

input_filename = "input.txt"
output_filename = "output.txt"

try:
    with open(input_filename, "r") as infile:
        lines = infile.readlines()

    with open(output_filename, "w") as outfile:
        for line_number, line in enumerate(lines, start=1):
            modified_line = f"{line_number}: {line.upper()}"
            outfile.write(modified_line)

    print(f"Modified content written to '{output_filename}' successfully.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied while accessing '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
