import React, { useEffect, useState } from "react";
import axios from "axios";

function Projects({ token }) {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/projects/", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(res => setProjects(res.data))
    .catch(err => console.error(err));
  }, [token]);

  return (
    <div>
      <h2>Your Projects</h2>
      <ul>
        {projects.map(p => (
          <li key={p.id}>{p.title}: {p.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default Projects;
