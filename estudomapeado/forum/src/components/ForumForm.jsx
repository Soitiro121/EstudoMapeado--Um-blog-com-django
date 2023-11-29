import React, { useState } from 'react';

const ForumForm = () => {
  const [newMessage, setNewMessage] = useState('');

  const handleFormSubmit = async event => {
    event.preventDefault();

    // Make a POST request to your API to add a new message
    try {
      const response = await fetch('http://your-api-url/api/v1/forummessages/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: newMessage }),
      });

      // Handle the response as needed
      console.log('New message added:', response);
    } catch (error) {
      console.error('Error adding new message:', error);
    }
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <textarea
        value={newMessage}
        onChange={e => setNewMessage(e.target.value)}
        placeholder="Type your message..."
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default ForumForm;
