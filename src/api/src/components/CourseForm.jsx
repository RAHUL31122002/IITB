import React, { useEffect, useState } from "react";
import api from "../api/api";

const CourseForm = () => {
  const [title, setTitle] = useState("");
  const [courseID, setCourseID] = useState("");
  const [description, setDescription] = useState("");
  const [prereqs, setPrereqs] = useState([]);
  const [allCourses, setAllCourses] = useState([]);

  useEffect(() => {
    api.get("/courses").then(res => setAllCourses(res.data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("/courses", {
      course_id: courseID,
      title,
      description,
      prerequisites: prereqs,
    }).then(() => {
      alert("Course Created!");
    }).catch(err => alert(err.response.data.error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Course ID" value={courseID} onChange={e => setCourseID(e.target.value)} required />
      <input placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} required />
      <textarea placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} />
      <select multiple value={prereqs} onChange={e => setPrereqs([...e.target.selectedOptions].map(o => o.value))}>
        {allCourses.map(course => (
          <option key={course.course_id} value={course.course_id}>
            {course.course_id} - {course.title}
          </option>
        ))}
      </select>
      <button type="submit">Create Course</button>
    </form>
  );
};

export default CourseForm;
