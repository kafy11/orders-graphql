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


class EquivalencyGroup(Base):
    __tablename__ = 'IGS_EQUIVALENCY_GROUP'
    companyId = Column('id_company_fk', Integer, primary_key=True)
    equivalencyGroupId = Column('id_equivalency_group_pk', Integer, primary_key=True)
    name = Column('EQUIVALENCY_GROUP_NAME', String)

class AGEncoded(Base):
    __tablename__ = 'IGS_AG_ITEMS_ENCODED'
    companyId = Column('id_company_fk', Integer, primary_key=True)
    organizationId = Column('id_organization_fk', Integer, primary_key=True)
    equivalencyGroupId = Column('id_equivalency_group_fk', Integer, primary_key=True)
    m0 = Column(Integer)
    m1 = Column(Integer)
    m2 = Column(Integer)
    m3 = Column(Integer)
    m4 = Column(Integer)
    m5 = Column(Integer)
    m6 = Column(Integer)
    m7 = Column(Integer)
    m8 = Column(Integer)
    m9 = Column(Integer)
    m10 = Column(Integer)
    m11 = Column(Integer)
    m12 = Column(Integer)
    average = Column(Integer)
    total12m = Column('total_12m', Integer)
    
    __table_args__ = (ForeignKeyConstraint([companyId, equivalencyGroupId],
                                           [EquivalencyGroup.companyId, EquivalencyGroup.equivalencyGroupId]),
                      {})
    equivalencyGroup = relationship(
        EquivalencyGroup,
        backref=backref('equivalencyGroups',
                        uselist=True,
                        cascade='delete,all'))