import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    file_path1 = open(file_path).read()
    dict1 = json.loads(file_path1)
    return dict1

print(read_data('data/result.json'))