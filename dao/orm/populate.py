from dao.orm.model import *
from dao.db import PostgresDb

db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

session.query(Child).delete()
session.query(Parent).delete()

parent1 = Parent(id=1)
parent2 = Parent(id=2)
parent3 = Parent(id=3)

child1 = Child(id=1)
child2 = Child(id=2)
child3 = Child(id=3)

session.add_all([parent1, parent2, parent3, child1, child2, child3])
session.commit()