def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(build_profile("Anuraag","Shukla",hobbies=["Gaming","Reading"],age=23,areas_of_interest=["Artificial Intelligence","Data Science"]))