import json

def readJsonFile(file_path):
    """
    Reads a JSON file and returns the data as a dictionary.
    :param file_path: Path to the JSON file
    :return: Dictionary containing the JSON data
    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        data = {}
    return data