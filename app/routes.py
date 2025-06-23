from flask import Blueprint, request, jsonify
from db_config import db
from models import Course, CoursePrerequisite, CourseInstance

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    course_id = data.get('course_id')
    title = data.get('title')
    description = data.get('description')
    prerequisites = data.get('prerequisites', [])

    # Check if all prerequisites exist
    for pid in prerequisites:
        if not Course.query.filter_by(course_id=pid).first():
            return jsonify({"error": f"Invalid prerequisite: {pid}"}), 400

    course = Course(course_id=course_id, title=title, description=description)
    db.session.add(course)
    db.session.commit()

    for pid in prerequisites:
        prereq = CoursePrerequisite(course_id=course_id, prerequisite_id=pid)
        db.session.add(prereq)
    db.session.commit()

    return jsonify({"message": "Course created successfully"}), 201
