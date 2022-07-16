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
    for k,q in data.items():
        if k == "name":
            user_list.append([q])
    return user_list
print(find_all_users_id(read_data))