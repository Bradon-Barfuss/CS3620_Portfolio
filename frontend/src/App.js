import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import ContactForm from './components/ContactForm';
import Project from './components/Project';
import ProjectShowcase from './components/ProjectShowcase';
import Base from './components/Base';

function App() {
  return (
    <Router>
      <Base>
        <Routes>
          <Route path="/" element={<Project />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/Project" element={<Project />} />
          <Route path="/Project/:id" element={<ProjectShowcase />} />
          <Route path="/contact" element={<ContactForm />} />
        </Routes>
      </Base>
    </Router>
  );
}

export default App;
