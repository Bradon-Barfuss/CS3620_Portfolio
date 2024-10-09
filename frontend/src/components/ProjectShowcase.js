// ProjectShowcase.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const ProjectShowcase = () => {
  const { id } = useParams();
  const [project, setProject] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/Project/${id}/`)
      .then(response => setProject(response.data))
      .catch(error => console.error(error));
  }, [id]);

  return (
    project && (
      <div className="project-display container mt-5">
        <div className="row">
          <div className="col-md-7">
            <h1>{project.project_name}</h1>
            <h4>Language: {project.project_language}</h4>
            <h3>Project Highlights</h3>
            <ul>
              {project.project_highlights.map((highlight, index) => (
                <li key={index}>{highlight}</li>
              ))}
            </ul>
          </div>
          <div className="col-md-5 text-right">
            <img src={project.project_image} alt={project.project_name} />
          </div>
        </div>
        <div className="row mb-4">
          <div className="col-md-12">
            <h3>Key Features</h3>
            <ul>
              {project.features.map((feature, index) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </div>
        </div>
        <div className="row mb-5">
          <div className="col-md-12">
            <h3>Implementation Details</h3>
            <ul>
              {project.implementation_details.map((detail, index) => (
                <li key={index}>{detail}</li>
              ))}
            </ul>
          </div>
        </div>
        <div className="row mt-5">
          <div className="col-md-12 d-flex justify-content-between">
            {project.github_link && (
              <a href={project.github_link} target="_blank" className="btn btn-dark">View on GitHub</a>
            )}
            <a href="/Project" className="btn btn-secondary">Back to Projects</a>
          </div>
        </div>
      </div>
    )
  );
}

export default ProjectShowcase;
