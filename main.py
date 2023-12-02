from fastapi import FastAPI

from comments.comment_api import comment_router
from product.product_api import product_router
from user.user_api import user_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(comment_router)

@app.get('/test')
async def test():
    return 'This is test page'
