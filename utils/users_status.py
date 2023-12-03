class UsersInGame:

    USERS = set()

    @classmethod
    def add_user(cls, user_id: int) -> bool:
        if not isinstance(user_id, int):
            return False

        cls.USERS.add(user_id)
        return True

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        if not isinstance(user_id, int):
            return False

        try:
            cls.USERS.remove(user_id)
        except KeyError:
            return False
        else:
            return True

__all__ = (
    'UsersInGame',
)
