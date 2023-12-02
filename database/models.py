from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship

from database import Base



class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)



class UserProduct(Base):
    __tablename__ = 'products'
    products_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    products_text = Column(String)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy="subquery")

class Comment(Base):
    __tablename__ = 'product_comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    products_id = Column(Integer, ForeignKey('products.products_id'))
    comment_text = Column(String)

    user_fk = relationship(User, lazy='subquery')
    products_fk = relationship(UserProduct, lazy='subquery')

