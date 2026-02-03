from ulid import ULID
from datetime import datetime
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from user.domain.user import User, Profile
from utils.crypto import Crypto
from common.exceptions import BusinessException

class UserService:
    def __init__(self):
        self.user_repo : IUserRepository = UserRepository()
        self.ulid = ULID()
        self.crypto = Crypto()

    def create_user(self, name: str, email: str, password: str):
        _user = None

        try:
            _user = self.user_repo.find_by_email(email)
        except BusinessException as e:
            if e.code_name != "USER_NOT_FOUND":
                raise e
        
        if _user:
            raise BusinessException("USER_ALREADY_EXISTS")

        now = datetime.now()
        user : User = User(
            id=self.ulid.generate(),
            profile=Profile(name=name, email=email),
            password=self.crypto.encrypt(password),
            created_at=now,
            updated_at=now)

        self.user_repo.save(user)

        return user