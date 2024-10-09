// ContactForm.js
import React, { useState } from 'react';
import axios from 'axios';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    contact_name: '',
    contact_email: '',
    contact_message: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/contacts/', formData)
      .then(response => console.log(response.data))
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input type="text" name="contact_name" value={formData.contact_name} onChange={handleChange} required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" name="contact_email" value={formData.contact_email} onChange={handleChange} required />
      </div>
      <div>
        <label>Message:</label>
        <textarea name="contact_message" value={formData.contact_message} onChange={handleChange} required></textarea>
      </div>
      <button type="submit">Save</button>
    </form>
  );
}

export default ContactForm;
