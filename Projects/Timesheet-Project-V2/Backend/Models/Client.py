class Client:
    client_list = []

    def __init__(self, client_id, client_name, client_description):
        self.client_id = client_id
        self.client_name = client_name
        self.client_description = client_description
        client_list = [self.client_id, self.client_name, self.client_description]
        Client.client_list.append(client_list)

    @classmethod
    def get_client_list(cls):
        return cls.client_list

    @classmethod
    def add_client(cls, client):
        cls.client_list.append(client)

    @classmethod
    def remove_client(cls, client_id):
        for client in cls.client_list:
            if client[0] == client_id:
                cls.client_list.remove(client)
                break

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_client_name(self):
        return self.client_name

    def set_client_name(self, client_name):
        self.client_name = client_name

    def get_client_description(self):
        return self.client_description

    def set_client_description(self, client_description):
        self.client_description = client_description

    @classmethod
    def empty_client_list(cls):
        cls.client_list = []
