from pydantic import BaseModel


class PublicProductValidator(BaseModel):
    user_id: int
    product_text: str

class EditProductValidator(BaseModel):
    product_id: int
    new_text: str
    user_id: int
