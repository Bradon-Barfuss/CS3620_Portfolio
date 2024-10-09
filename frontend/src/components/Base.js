// Base.js
import React from 'react';
import { Link } from 'react-router-dom';

const Base = ({ children }) => {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">Bradon Barfuss Portfolio</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar_Home">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbar_Home">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/Project">Project</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/contact">Contact</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div>{children}</div>

      <footer className="footer bg-dark text-light mt-5">
        <div className="container py-4">
          <div className="row">
            <div className="col-md-8">
              <h5>About Me</h5>
              <p>Hi! I'm Bradon Barfuss, a passionate software developer with experience in full-stack development, machine learning, Object-Oriented Programming, and cloud-based development.</p>
            </div>
            <div className="col-md-2">
              <h5>Quick Links</h5>
              <ul>
                <li><Link to="/Project">Project</Link></li>
                <li><Link to="/contact">Contact</Link></li>
              </ul>
            </div>
            <div className="col-md-2">
              <h5>Connect with Me</h5>
              <a href="https://github.com/Bradon-Barfuss" className="text-light me-2" target="_blank">GitHub</a>
              <a href="https://linkedin.com/in/bradonbarfuss" className="text-light" target="_blank">LinkedIn</a>
            </div>
          </div>
          <div className="row">
            <div className="col-md-12 text-center">
              <p>&copy; 2024 Bradon Barfuss - All Rights Reserved</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Base;
