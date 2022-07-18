from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    list1 = []
    for i in data['messages']:
        if i.get("actor"):
            if i['actor'] not in list1:
                list1.append([i['actor']])
        if i.get("from"):
            if i['from'] not in list1:
                list1.append([i['from']])
    return list1
