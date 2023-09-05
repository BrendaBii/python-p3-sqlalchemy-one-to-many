from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Session = sessionmaker(bind=engine)
#session = Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'

# # Access the first review instance in the database
# review = session.query(Review).first()
# review
# # => Review(id=1, score=7, game_id=1)

# # Get the game_id foreign key for the review instance
# review.game_id
# # => 1

# # Find a specific game instance using an ID
# session.query(Game).filter_by(id=review.game_id).first()
# # => Game(id=1, title=Jacob Floyd, platform=wii u)

# review.game

# game = session.query(Game).first()
# game

# reviews = session.query(Review).filter_by(game_id=game.id)
# [review for review in reviews]
# # => [Review(id=1, score=7, id=1), Review(id=2, score=7, id=1), Review(id=3, score=8, id=1)]

# game.reviews