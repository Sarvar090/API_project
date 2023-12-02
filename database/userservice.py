from database.models import User

from database import get_db

from datetime import datetime



def register_user_db(name, surname, email,
                     phone_number, city, password,reg_date):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return 'Такой пользователь уже есть'

    new_user = User(name=name, surname=surname, email=email,
                    phone_number=phone_number, city=city, password=password,
                    reg_date=datetime.now())
    db.add(new_user)
    db.commit()

    return 'Успешно прошли регистрацию'


def check_user_email_db(email):
    db= next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return 'Нет такого email!'


def login_user_db(email, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    else:
        return 'Ошибка в данных'



def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user


def edit_user_db(user_id , edit_type, new_data):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'password':
            exact_user.password = new_data
        elif edit_type == 'city':
            exact_user.city = new_data

        db.commit()

        return 'Данные успешно изменены'

    else:
        return 'Пользователь не найден'


def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()
        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'

