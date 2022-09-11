from faker import Faker
from sqlalchemy import update
from sqlalchemy.orm import joinedload

from src.db import session
from src.models import User, Phone, Email

fake = Faker('uk_UA')


def add_user(*args, **kwargs):
    user = User(name=kwargs['name'], address=kwargs['address'])
    phone = Phone(phone_number=kwargs['phone'])
    email = Email(email=kwargs['email'])
    user.phone.append(phone)
    user.email.append(email)
    session.add(user)
    session.commit()
    return f'User {user.name} added successfully!'


def update_user(*args, **kwargs):
    user_id = kwargs['id']
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.execute(update(User).where(User.id == user_id).values(name=kwargs['name'], address=kwargs['address'],
                                                                      phone=kwargs['phone'], email=kwargs['email']))
        session.commit()
        return f'User {user.name} updated successfully!'
    return f'User with id {user_id} not found!'


def delete_user(*args, **kwargs):
    user = session.query(User).filter(User.id == kwargs['id']).first()
    session.delete(user)
    session.commit()
    return f'User {user.name} deleted successfully!'


def get_user(*args, **kwargs):
    user_id = kwargs['id']
    user = session.query(User).options(joinedload(User.phone), joinedload(User.email)).filter(
        User.id == user_id).first()
    return f'User: {user.name}, Phone: {user.phone[0].phone_number}, Email: {user.email[0].email}, Address: {user.address}'


def get_all_users(*args, **kwargs):
    users = session.query(User).options(joinedload(User.phone), joinedload(User.email)).all()
    return '\n'.join([
        f'User: {user.name}, Phone: {user.phone[0].phone_number}, Email: {user.email[0].email}, Address: {user.address}'
        for user in users])


def add_random_users(*args, **kwargs):
    for _ in range(100):
        user = User(name=fake.name(), address=fake.address())
        phone = Phone(phone_number=fake.phone_number())
        email = Email(email=fake.email())
        user.phone.append(phone)
        user.email.append(email)
        session.add(user)
    session.commit()
