class User:
    __user_list = []

    def __init__(self, u_id, name, surname, email, hashpassword, etype):
        self.__id = u_id
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__hashpassword = hashpassword
        self.__etype = etype
        self.clear_user_list()  # Clear the user list before adding a new user
        self.add_user()

    def add_user(self):
        if len(User.__user_list) == 0:  # Only add the user if the list is empty
            User.__user_list.append(self)

    @classmethod
    def get_user(cls):
        if len(cls.__user_list) > 0:
            return cls.__user_list[0]
        else:
            return None

    @classmethod
    def clear_user_list(cls):
        cls.__user_list = []

    # Getter and setter methods for the fields
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_hashpassword(self):
        return self.__hashpassword

    def set_hashpassword(self, hashpassword):
        self.__hashpassword = hashpassword

    def get_etype(self):
        return self.__etype

    def set_etype(self, etype):
        self.__etype = etype
