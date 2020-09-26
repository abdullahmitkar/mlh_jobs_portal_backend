from db_module.db_main import Base
from sqlalchemy import Column, Integer, String, BigInteger


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column("name", String(50))
    password = Column("password", String(20))
    portal = Column("portal", String(50))
    # address = Column("address", String(200))
    # mobile = Column("mobile", BigInteger)
    # user_detail = Column("user_detail", String(8))


    def __init__(self, name, password, portal):
        self.name = name
        self.password = password
        self.portal = portal
