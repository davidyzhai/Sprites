#David Zhai
#1/17/2024
#This program is a python script which provides the functionality of a multiclipboard. 
#The user's current clipboard content can be saved to a key. 
#This key can later be loaded, and the corresponding clipboard content will be copied.
#The user may also use the list command to see all saved data, and the corresponding keys. 
import sys
import clipboard
import json

# Define the file path for saving and loading data
SAVED_DATA = "clipboard.json"

# Function to save data to a specified file path
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Function to load data from a specified file path
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# Check if a command-line argument is provided. There should be two only.
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    #handle different commands
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command. Valid commands include save, load, or list.")
