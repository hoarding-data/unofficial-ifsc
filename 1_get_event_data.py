import os
import json

def find_json_files(directory):
    """
    Find all JSON files in the specified directory and its subdirectories.

    :param directory: The root directory to search in.
    :return: A list of paths to JSON files.
    """
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

def create_folder_if_not_exists(path):
    """
    Create a folder at the specified path if it does not exist.

    :param path: The path where the folder should be created.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        #print(f"Folder created at {path}")
    else:
        pass;
        #print(f"Folder already exists at {path}")

def save_event_data(event_key, event_data, output_directory):
    """Save event data to a JSON file."""
    output_path = os.path.join(output_directory, f"{event_key}.json")
    with open(output_path, 'w') as file:
        json.dump(event_data, file, indent=4)
    print(f"Event data saved to {output_path}")

if __name__ == "__main__":
    directory_to_search = "ifsc_year_data"
    json_files = find_json_files(directory_to_search)
    print("Found JSON files:")
    json_files.sort(reverse=True)
    for file in json_files:
        filename = file.split("/")[-1]
        year = filename.split("_")[1]
        print(year)
        event_folder_path = "{}/{}_event_data".format(directory_to_search,year)
        create_folder_if_not_exists(event_folder_path)
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            events = data.get('events', {})
            for event_key, event_data in events.items():
                save_event_data(event_key, event_data, event_folder_path)


