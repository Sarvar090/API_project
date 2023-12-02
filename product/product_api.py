from fastapi import APIRouter, UploadFile, Body

from product import PublicProductValidator, EditProductValidator

from database.productservice import (add_product_db,edit_product_db, delete_product_db,get_all_product_db,
                                     get_exact_product_db)

product_router = APIRouter(prefix='/products', tags=['Работа с продуктами'])



@product_router.post('/public_product')
async def public_product(data: PublicProductValidator):
    result = add_product_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Не найдено!'}


@product_router.put('/change_product')
async def change_product(data: EditProductValidator):
    result = edit_product_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Не найдено!'}



@product_router.delete('/delete_product')
async def delete_product(products_id: int):
    result = delete_product_db(products_id)

    if result:
        return {'message': result, 'status': 'Deleted'}
    else:
        return {'message': 'Не найдено!'}


# Запрос на получения всех публикаций
@product_router.get('/get_all_products')
async def get_all_products(products_id: int):
    result = get_all_product_db()

    return {'message': result}


# Получить определенный пост
@product_router.get('/get_exact_product')
async def get_exact_product(products_id: int):
    result = get_exact_product_db(products_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Не найдено!'}