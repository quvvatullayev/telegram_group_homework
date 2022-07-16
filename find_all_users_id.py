from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    user_list = []
    for k in data['messages']:
        if k == "from_id":
            user_list.append(k['from_id'])
    return user_list
print(find_all_users_id(read_data))