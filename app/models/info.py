from app.models import BaseModel
from app.extensions import db


class University(db.Model, BaseModel):
    __tablename__ = "universities"

    id = db.Column(db.Integer, primary_key=True)
    university_name = db.Column(db.String)
    location = db.Column(db.String)
    website_url = db.Column(db.String)
    contact_email = db.Column(db.String)
    contact_phone = db.Column(db.String)
    overview = db.Column(db.Text)
    established_year = db.Column(db.DateTime)
    logo_url = db.Column(db.String)


class Program(db.Model, BaseModel):
    __tablename__ = "programs"

    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String)
    une_code = db.Column(db.String)
    university_id = db.Column(db.ForeignKey("universities.id"))
    university = db.relationship("University", uselist=False)
    level = db.Column(db.String)
    desc = db.Column(db.Text)
    duration = db.Column(db.Integer)
    requirements = db.Column(db.Text)
    tuition_fee = db.Column(db.Float)
    program_url = db.Column(db.String)


class Review(db.Model, BaseModel):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    university_id = db.Column(db.ForeignKey("universities.id"))
    university = db.relationship("University", uselist=False)
    user_id = db.Column(db.ForeignKey("users.id"))
    user = db.relationship("User", uselist=False)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.Text)








