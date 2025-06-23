from db_config import db

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(10), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    prerequisites = db.relationship(
        'CoursePrerequisite',
        foreign_keys='CoursePrerequisite.course_id',
        cascade="all, delete",
        backref='course'
    )

class CoursePrerequisite(db.Model):
    __tablename__ = 'course_prerequisites'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(10), db.ForeignKey('courses.course_id'))
    prerequisite_id = db.Column(db.String(10), db.ForeignKey('courses.course_id'))

class CourseInstance(db.Model):
    __tablename__ = 'course_instances'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(10), db.ForeignKey('courses.course_id'))
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
