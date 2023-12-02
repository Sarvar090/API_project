from pydantic import BaseModel


# Валидатор для публикаций коммента
class CommentValidator(BaseModel):
    comment_text: str
    user_id: int
    post_id: int


# Валидатор для изменения комента
class EditCommentValidator(BaseModel):
    new_text: str
    comment_id: int
