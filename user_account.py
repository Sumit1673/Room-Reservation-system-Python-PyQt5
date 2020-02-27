import json as js


def open_file(_mode='r'):
    try:
        with open("user_details.json", _mode) as user_data_file:
            return user_data_file
    except FileNotFoundError:
        print("user_details.json not found")


class UserAccount:
    def __init__(self):
        self.user_data = None

    def __repr__(self):
        return "UserAccount <class> to validate and store user details"

    def validation(self, username: str, password: str):
        found = False
        for users in self.load_database():

            found = [True if username == users['username'] and password == users['password'] else False]
            if found[0]:
                break
        return found[0]

    def register_user(self, *, full_name, email, username, password):
        if self.validation(username, password) is False:
            done = self.add_user(full_name, email, username, password)
            if done:
                print("User Added")

    def add_user(self, full_name, email, username, password):
        try:
            with open("user_details.json", 'r') as user_data_file:
                users_dict = js.load(user_data_file)
                new_user = {"username": username, "full_name": full_name,
                            "email": email, "password": password}
                users_dict.append(new_user)
        except Exception as e:
            print(e)
        try:
            with open("user_details.json", 'w') as user_data_file2write:
                js.dump(users_dict, user_data_file2write, indent=2, ensure_ascii=False)
                user_data_file2write.write('\n')
                return True
        except Exception as e:
            print(e)

    def delete_user(self):
        pass

    def load_database(self):
        try:
            with open("user_details.json", 'r') as user_data_file:
                self.user_data = js.load(user_data_file)
                for each_user in self.user_data:
                    yield each_user
        except FileNotFoundError:
            print("user_details.json not found")


if '__main__' == __name__:
    u = UserAccount()
    print(u)
    # u.register_user(full_name='Jason', email="json.stathom@gmail.com",
    #                 username="Jason11", password="Iamexpendable")