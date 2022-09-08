from sqlalchemy import update

from src.db import session
from src.models import User


def add_user(*args, **kwargs):
    user = User(**kwargs)
    session.add(user)
    session.commit()
    return f'Added user {user.name} to the database.'


def update_user(*args, **kwargs):
    user_id = kwargs.pop('id')
    user = session.get(User, user_id)
    if user:
        session.execute(update(User).where(User.id == user_id).values(**{k: v for k, v in kwargs.items() if v}))
        session.commit()
        return f'Updated user {user.id} in the database.'
    return f'User with id {user_id} not found.'


def delete_user(*args, **kwargs):
    user_id = kwargs.pop('id')
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return f'Deleted user {user.name} from the database.'
    return f'User with id {user_id} not found.'


def get_user(*args, **kwargs):
    user_id = kwargs.pop('id')
    user = session.get(User, user_id)
    if user:
        return f'User with id {user_id} found: {user.name}, {user.phone}, {user.email}, {user.address}'
    return f'User with id {user_id} not found.'


def get_all_users(*args, **kwargs):
    users = session.query(User).all()
    return '\n'.join([f'{user.name}, {user.phone}, {user.email}, {user.address}' for user in users])