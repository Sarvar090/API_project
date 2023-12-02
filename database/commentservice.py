from .models import Comment

from datetime import datetime

from database import get_db



def add_comment_db(user_id, comment_text, products_id):
    db = next(get_db())

    new_comment = Comment(products_id=products_id, comment_text=comment_text, user_id=user_id)

    db.add(new_comment)
    db.commit()

    return "Коментарий успешно добавлен"


def edit_comment_db(comment_id, new_comment):
    db = next(get_db())

    edit_comment = db.query(Comment).filter_by(comment_id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = new_comment
        db.commit()

        return 'Коментарий успешно изменен'
    else:
        return False



def delete_comment_db(comment_id):
    db = next(get_db())

    delete_comment = db.query(Comment).filter_by(comment_id=comment_id).first()

    if delete_comment:
        db.delete(delete_comment)
        db.commit()

        return "Успешно удален"
    else:
        return False


def get_products_comments(products_id):
    db = next(get_db())

    products_comment = db.query(Comment).filter_by(products_id=products_id).first()
    return products_comment
