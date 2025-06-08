import requests
import os

url = "https://pixplet.com/pixplet-dataset.json"
local_path = "pixplet-dataset.json"

def download_and_update():
    response = requests.get(url)
    response.raise_for_status()
    new_data = response.text

    if os.path.exists(local_path):
        with open(local_path, "r", encoding="utf-8") as f:
            current_data = f.read()
        if current_data.strip() == new_data.strip():
            print("No changes detected.")
            return

    with open(local_path, "w", encoding="utf-8") as f:
        f.write(new_data)
    print("Dataset updated.")

if __name__ == "__main__":
    download_and_update()
