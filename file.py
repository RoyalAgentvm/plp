def modify_content(content):
    """Example modification: Convert text to uppercase and add line numbers"""
    lines = content.split('\n')
    modified = []
    for i, line in enumerate(lines, 1):
        modified.append(f"{i:03d} {line.upper()}")
    return '\n'.join(modified)

def main():
    # Get filenames from user
    input_file = input("Enter input filename: ").strip()
    output_file = input("Enter output filename: ").strip()

    try:
        # Attempt to read input file
        with open(input_file, 'r') as f:
            original_content = f.read()
            
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_file}'.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode '{input_file}' as text file.")
    except Exception as e:
        print(f"Unexpected error reading file: {str(e)}")
    else:
        try:
            # Process content and write output
            new_content = modify_content(original_content)
            
            with open(output_file, 'w') as f:
                f.write(new_content)
                
            print(f"Success! Modified content written to '{output_file}'")
            
        except PermissionError:
            print(f"Error: Permission denied to write to '{output_file}'.")
        except IsADirectoryError:
            print(f"Error: '{output_file}' is a directory, not a file.")
        except Exception as e:
            print(f"Unexpected error writing file: {str(e)}")

if __name__ == "__main__":
    main()