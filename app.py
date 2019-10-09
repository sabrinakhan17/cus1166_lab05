import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    course = Course.query.all()
    return render_template('index.html', course = course)

@app.route("/add_course", methods=["POST"])
def add_course():
    id = request.form.get("id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course = Course(id = id ,course_number= number, course_title = title)
    db.session.add(course)
    db.session.commit()
    course = Course.query.all()
    return render_template('index.html', course = course)

@app.route("/register_student/<int:course_id>", methods=['GET', 'POST'])
def register_student(course_id):
    course = Course.query.get(course_id)
    if request.method == 'GET':
        return render_template('course_details.html', course=course)
    elif request.method == 'POST':
        id = id.request.form.get("id")
        name = name.request.form.get("name")
        grade = grade.request.form.get("grade")
        course.add_student(id, name, grade)
    students = course.students
    return render_template("course_details.html", course = course, students = students)

def main():
    if (len(sys.argv) == 2):
        print(sys.argv)
    if sys.argv[1] == 'createdb':
        db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use python app.py createdb")

if __name__ == "__main__":
     with app.app_context():
        main()
