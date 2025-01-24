from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = 'localhost'
port = '5432'
user = 'postgres'
password = '123123'
database = 'BPTFO-20-IT-2'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# 'postgresql+psycopg2://postgres:123123@localhos:5432/BPTFO-20-IT-2'

Base = declarative_base()

class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cityname = Column(String(30), nullable=False)

    def __init__(self, cityname):
        self.cityname = cityname


class AccountTypes(Base):

    __tablename__ = 'accounttypes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    accounttypename = Column(String(30), nullable=False)


class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    idnumber = Column(String(11), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    dateofbirth = Column(Date)
    cityid = Column(Integer, ForeignKey('cities.id'))
    zipcode = Column(String(4))
    street = Column(String(50))
    housenumber = Column(Integer)
    income = Column(Float)
    create_date = Column(DateTime)
    update_date = Column(DateTime)


    # def __repr__(self):
    #     return f'({self.idnumber}, {self.first_name}, {self.last_name})'


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customeridnumber = Column(String(11), ForeignKey('customers.idnumber'), nullable=False)
    accountnumber = Column(String(50), nullable=False)
    accounttypeid = Column(Integer, ForeignKey('accounttypes.id'), nullable=False)
    balance = Column(Float, nullable=False)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()