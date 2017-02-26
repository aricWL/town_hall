from project import db




class TownHall(db.MODEL):

    __tablename__ = 'townhalls'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.Text)



    def __init__(self, name):
        self.name = name


class Representative(db.MODEL):

    __tablename__ = 'representatives'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.Text)
    town_hall = db.Column(db.Integer)


    def __init__(self, name, town_hall):
        self.name = name
        self.town_hall = town_hall

class Questions(db.MODEL):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question  = db.Column(db.Text)
    town_hall = db.Column(db.Integer)


    def __init__(self, question, town_hall):
        self.question = question
        self.town_hall = town_hall