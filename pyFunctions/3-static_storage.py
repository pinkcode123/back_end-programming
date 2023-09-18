storage=[{
    'name':'Gentle',
    'sex':'male',
    'mobile': '08123456647'

}]
def new_user(name,sex,mobile):
    my_user = {'name': name,
               "sex" : sex,
               "mobile" :mobile
               }
    storage.append(my_user)
    print(storage)
user_name = input("Enter username $ ")
user_sex = input("Enter usersex $ ")
user_mobile = input("Enter mobile")
new_user(user_name,user_sex,user_mobile)

