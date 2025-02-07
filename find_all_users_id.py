from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    list_print = []
    for i in data["messages"]:
        if i.get('from_id'):
            if i['from_id'] not in list_print:
                list_print.append(i['from_id'])

    return list_print