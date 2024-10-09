// Projects.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Project = () => {
  const [Project, setProject] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/project/')
      .then(response => setProject(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-5">
      <div className="row">
        {Project.map(item => (
          <div className="project-card" key={item.id}>
            <div className="col-md-4">
              <img className="card-img" src={item.project_image} alt={item.project_name} />
            </div>
            <div className="col-md-4">
              <h3>{item.project_name}</h3>
              <h4><b>Language: </b>{item.project_language}</h4>
              <h6><b>Description: </b>{item.project_desc}</h6>
            </div>
            <div className="col-md-3 mt-3">
              <div className="d-flex justify-content-start gap-2">
                <a href={`/Project/${item.id}`} className="btn btn-success">Details</a>
                <a href={item.github_link} target="_blank" className="btn btn-dark">View on GitHub</a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Project;
