import os

def read_and_modify_file():
    """
    Reads a file from user input, modifies its content, and writes to a new file.
    Handles potential errors during the process.
    """
    try:
        # Prompt user for input filename
        input_filename = input("Enter the name of the file you want to read: ").strip()
        
        # Check if file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Write modified content to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File successfully processed!")
        print(f"Original file: {input_filename}")
        print(f"Modified file: {output_filename}")
        
        # Optional: Display modified content
        print("\n--- Modified Content ---")
        print(modified_content)
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        print("Please check the filename and try again.")
    
    except PermissionError:
        print("Error: You don't have permission to read or write this file.")
    
    except IOError as io_error:
        print(f"An I/O error occurred: {io_error}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("🖋️ File Read & Write Challenge 🧪")
    print("This program reads a file, modifies its content, and writes to a new file.")
    
    while True:
        read_and_modify_file()
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want to process another file? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the File Read & Write Challenge!")
            break

if __name__ == "__main__":
    main() 