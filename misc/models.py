def create_classes(db):
    class Grade(db.Model):
        __tablename__ = 'loan_grades'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        loan_score = db.Column(db.Float)
        loan_amount = db.Column(db.Float)

        def __repr__(self):
            return 'loan_grades'
    return Grade
