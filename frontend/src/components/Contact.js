// Contact.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Contact = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/contacts/')
      .then(response => setContacts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-5">
      <div className="row">
        {contacts.map(contact => (
          <div className="project-card" key={contact.id}>
            <div className="col-md-4">
              <h3>{contact.contact_name}</h3>
              <h4>{contact.contact_email}</h4>
              <p>{contact.contact_message}</p>
              <h4><a href={`/contact/${contact.id}/edit`} className="btn btn-success">Edit</a></h4>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Contact;
