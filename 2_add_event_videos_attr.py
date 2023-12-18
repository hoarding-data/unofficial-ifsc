import os
import json

def process_json_files(year):
    directory = f'ifsc_year_data/{year}_event_data'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                print(file)
                file_path = os.path.join(directory,file)
                with open(file_path, 'r') as fh:
                    data = json.load(fh)

                # Assuming 'categories' is a top-level key in the JSON structure.
                # Modify as necessary if 'categories' is located elsewhere.
                categories = data.get('categories', [])

                if data.get('event_videos') != None:
                    raise Exception("Event videos already found")
                # Create event_videos entries
                event_videos = []
                for category in categories:
                    event_videos.append({
                        "event_name": category,
                        "original_url": "",
                        "ipfs_cid": ""
                    })

                # Add event_videos to the data and write back to the file
                data['event_videos'] = event_videos
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)

                print(f"Processed file: {file_path}")

for year in range(1992,2024):
    process_json_files(year)
