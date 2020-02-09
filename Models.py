from typing import Type
import PasswordMaker
#import pymongo

class User:
    def __init__(self):
        self.username = Type[str]
        self.passwords = Type[dict]
        self.password = Type[str]

    def register(self):
        print('Registering:\n')
        self.username = self.read_username()
        self.password = self.read_password()
        print('Success')

    def add_password(self):
        password = Password()
        password_maker = PasswordMaker()

        password.key = self.get_key()
        password.value = password_maker.create_password()

    def authenticate_register(self):
        pass

    def authenticate(self, typed_username, typed_password):
        return typed_username is self.username and typed_password is self.username

    def login(self):
        username = self.read_password()
        password = self.read_password()

        if self.authenticate(username, password):
            pass
        self.login()

    @staticmethod
    def read_username():
        return str(input('Username: '))

    @staticmethod
    def read_password():
        return str(input('Password: '))

    @staticmethod
    def get_key():
        return str(input('Key for password: '))


class Password:
    def __init__(self):
        self.key = Type[str]
        self.value = Type[str]
