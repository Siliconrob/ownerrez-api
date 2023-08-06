import os
from dataclasses import dataclass


@dataclass
class OwnerRezApiUser:
    """Class for getting the user."""
    agent: str
    username: str
    token: str

    def get_auth(self):
        return self.username.strip(), self.token.strip()

    def headers(self):
        return {'user-agent': self.agent.strip()}

    def is_valid(self) -> bool:
        if self.username is None or self.username.strip() == "":
            raise Exception(f'Empty username')
        if self.token is None or self.token.strip() == "":
            raise Exception(f'Empty token')
        return True


def get_env_user() -> OwnerRezApiUser:
    return OwnerRezApiUser(agent=os.environ.get('owner_rez_user_agent', 'api_python_agent'),
                           username=os.environ.get('owner_rez_username', None),
                           token=os.environ.get('owner_rez_token', None))
