from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declaretive baase তৈরী করা হয়েছে
Base = declarative_base()

# Class তৈরী করা হয়েছে বা মডেল তৈরী করা হয়েছে। এটি টেবিল তৈরী করার জন্য ব্যবহার হয়।
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# এখানে echo=True দেয়া হয়েছে যেন এটি কি করছে তা দেখা যায়। ডাটাবেজ সংযোগ করা হয়েছে।
engine = create_engine('sqlite:///user.db', echo=True)

# table তৈরী করা
Base.metadata.create_all(engine)

#session তৈরী করা
Session = sessionmaker(bind=engine)
session = Session()

# ডাটা ইনসার্ট করা
new_user = User(name='Rahat', age=24)
session.add(new_user)
session.commit()


# data query
user = session.query(User).filter_by(name='Rahat').first()
print(f'User name: {user.name}, User age: {user.age}')
# data update
user.age = 25
session.commit()
# data delete
# session.delete(user)
# session.commit()
session.close()

