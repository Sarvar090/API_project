from fastapi import APIRouter
from datetime import datetime

from user import LoginUserValidator, RegisterUserValidator, EditUserValidator

from database.userservice import (login_user_db,register_user_db,check_user_email_db, get_exact_user_db,
                                  get_all_users_db,edit_user_db,delete_user_db)

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])

# Логин
@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_db(**data.model_dump())
    return {'message':result}

# Регистрация
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    new_user_data = data.model_dump()

    checker = check_user_email_db(data.email)

    if not checker:
        result = register_user_db(reg_date=datetime.now(), **new_user_data)
        return {'message': result}
    else:
        return {'message': 'Пользователь уже есть!'}


# Запрос на получения информаций о пользователе
@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'message': result}
    else:
        result = get_exact_user_db(user_id)

        return {'message': result}

@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model.dump()

    result = edit_user_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нету пользователя чтобы изменить'}

@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': 'Поьзователь успешно удален'}
    else:
        return {'message': 'Ошибка'}

