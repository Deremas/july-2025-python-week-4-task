# File Handling and Exception Handling in Python
# Author: Dereje Masresha
# Description: Asks user for filename, creates file if needed, modifies content, writes to new file, handles errors.

def create_file(filename):
    """Create a file with Python-related content if it doesn't exist."""
    content = """Python is a versatile programming language.
You can use lists, dictionaries, and sets effectively.
Functions help organize reusable code.
Exception handling prevents program crashes.
File handling allows reading and writing files.
"""
    try:
        with open(filename, 'x') as file:  # 'x' mode creates file, errors if it exists
            file.write(content)
        print(f"File '{filename}' created with Python-related content.")
    except FileExistsError:
        print(f"File '{filename}' already exists. Using existing file.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file(filename):
    """Read the content of a file safely."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def write_file(filename, content):
    """Write content to a new file safely."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Modified content successfully written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def modify_content(content):
    """Modify content (example: uppercase)."""
    return content.upper()

def main():
    # Ask user for input file name
    input_file = input("Enter the filename to read or create: ").strip()
    
    # Create file if it doesn't exist
    create_file(input_file)
    
    # Read file content
    content = read_file(input_file)
    
    if content:
        # Modify content
        modified_content = modify_content(content)
        
        # Ask user for output file name
        output_file = input("Enter the filename to save the modified content: ").strip()
        write_file(output_file, modified_content)

if __name__ == "__main__":
    main()