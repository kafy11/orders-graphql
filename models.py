from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
from sqlengine import connect

engine = connect()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Product(Base):
    __tablename__ = 'TB_PRODUCT'
    __table_args__ = {'sqlite_autoincrement': True}
    productId = Column('id_product_pk', Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

class Order(Base):
    __tablename__ = 'TB_ORDER'
    orderId = Column('id_order_pk', Integer, primary_key=True)
    productId = Column('id_product_fk', Integer)
    qty = Column(Integer)
    
    __table_args__ = (ForeignKeyConstraint([productId],
                                           [Product.productId]),
                      {})
    product = relationship(
        Product,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete,all'))