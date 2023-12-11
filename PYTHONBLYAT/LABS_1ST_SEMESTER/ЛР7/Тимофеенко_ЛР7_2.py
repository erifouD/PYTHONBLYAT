def create_user_list(user_dict):
    users = []
    for key, value in user_dict.items():
        users.append({key:value})
    return users


user_dict1 = {"name":"Nazar","age":18,"location":"Moskow"}
print(create_user_list(user_dict1)) #[{"name":"Nazar"},{"age":18},{"location":"Moskow"}]
