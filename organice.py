import os
import shutil

def organize_files(folder_path):
    # Create a dictionary to hold folder names
    folder_names = {}

    # Create a text file to store the names of all files
    with open("file_names.txt", "w") as file:
        for file_name in os.listdir(folder_path):
            file.write(file_name + "\n")

            if file_name.endswith(".py"):  # Skip .py files
                continue

            src = os.path.join(folder_path, file_name)
            if os.path.isfile(src):
                print(f"Processing file: {file_name}")
                
                # Split file name by underscore and get the first and second words after the third underscore
                split_name = file_name.split("_")
                if len(split_name) > 3:
                    folder_name = "_".join(split_name[3:5])
                else:
                    folder_name = "Others"  # If there are fewer than three underscores, use "Others"

                # Create the destination folder if it doesn't exist
                destination_folder = os.path.join(folder_path, folder_name)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Move the file to the corresponding folder
                try:
                    dst = os.path.join(destination_folder, file_name)
                    shutil.move(src, dst)
                    print(f"Moved {file_name} to {folder_name} folder.")
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_files(folder_path)
