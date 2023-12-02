from fastapi import APIRouter

from comments import CommentValidator, EditCommentValidator

from database.commentservice import add_comment_db, edit_comment_db, delete_comment_db, get_products_comments

comment_router = APIRouter(prefix='/comment', tags=['Работа с отзывами'])

# Запрос на публикацию коментария
@comment_router.post('/add_comment')
async def add_comment(data: CommentValidator):
    result = add_comment_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! Not Found'}

# Запрос на изменения коментарий
@comment_router.put('/edit_comment')
async def edit_comment(data: EditCommentValidator):
    result = edit_comment_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Sorry! Not Found'}


# Запрос на удаления коммента
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)

    if result:
        return {'message': result, 'status': 'Deleted'}
    else:
        return {'message': 'Post not found'}

# Запрос на получения коментариев к определенному посту
@comment_router.get('/get_comments')
async def get_comments(products_id: int):
    result = get_products_comments(products_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Post not found'}
