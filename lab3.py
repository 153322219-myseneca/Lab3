def write_name_to_file(name):
    file_name = name + ".txt"  # Create a file name with your name and .txt extension
    file_path = "/path/to/directory/" + file_name  # Specify the directory where you want to save the file
    
    with open(file_path, "w") as file:
        file.write(name)  # Write your name to the file
    
    print(f"File '{file_name}' has been created with your name.")
