from .models import UserProduct
from datetime import datetime

from database import get_db



def add_product_db(user_id, products_text):
    db = next(get_db())


    new_product = UserProduct(user_id=user_id,
                        products_text=products_text,
                        publish_date=datetime.now())
    db.add(new_product)
    db.commit()

    return 'Успешно добавлено'


def get_all_product_db():
    db = next(get_db())

    all_products = db.query(UserProduct).all()
    return all_products

def get_exact_product_db(products_id):
    db = next(get_db())
    exact_product = db.query(UserProduct).filter_by(products_id=products_id).first()

    if exact_product:
        return exact_product
    else:
        return 'Error'

def edit_product_db(products_id, new_product):
    db= next(get_db())
    edit_product = db.query(UserProduct).filter_by(products_id=products_id).first()

    if edit_product:
        edit_product.products_text = new_product
        db.commit()

        return 'Продукт успешно изменен'
    else:
        return False

def delete_product_db(products_id):
    db = next(get_db())

    delete_product = db.query(UserProduct).filter_by(products_id=products_id).first()

    if delete_product:
        db.delete(delete_product)
        db.commit()

        return "Продукт успешно удален"
    else:
        return False

