from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "Courses"
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)
    student = db.relationship("Student", backref="Courses", lazy=True)

    def add_student(self, name, grade):
        new_Student = Registered_Student(name = name, grade = grade, course_id = self.id)
        db.session.add(new_Student)
        db.session.commit()

class Registered_Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.String, nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey('Courses.id'), nullable = False)
