import logging
import json
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("File handling module loaded.")

file_path = "example.json"


def read_file(file_path):

    try:
        logging.info("Opening the file")

        data = []

        # If file exists and is not empty, load the JSON content
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    logging.warning(
                        "File exists but not a valid JSON.Starting fresh."
                        )

        # Append new entry
        data.append("Hey I have created this file")

        # Write updated data back to the file
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

        logging.info("Data written successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


read_file(file_path)
