from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    list_prin = {}
    for i in data['messages']:
        for  e in users_id:
            if i['actor_id'] == e:
                list_prin[e] = len(i)
    return list_prin
print(find_user_message_count(read_data, find_all_users_id))