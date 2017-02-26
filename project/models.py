from project import db




class TownHall(db.Model):

    __tablename__ = 'townhalls'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.Text)
    location = db.Column(db.Text)

    def __init__(self, name):
        self.name = name


class Representative(db.Model):

    __tablename__ = 'representatives'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.Text)
    townhall = db.relationship('TownHall', backref='representative',
                               lazy='dynamic')


    def __init__(self, name, townhall):
        self.name = name
        self.townhall = townhall



class Question(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question  = db.Column(db.Text)
    answer = db.Column(db.Text, nullable = True)
    townhall = db.relationship('TownHall', backref='question',
                                lazy='dynamic')


    def __init__(self, question, townhall):
        self.question = question
        self.townhall = townhall
