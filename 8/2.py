class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self._password_hash = hash(password)

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Invalid email: must contain '@'")
        self._email = value

    def check_password(self, password: str) -> bool:
        return hash(password) == self._password_hash


user = User("test@example.com", "secret")
print(user.email)
# print(user.password)  # AttributeError
print(user.check_password("secret"))
print(user.check_password("wrong"))
