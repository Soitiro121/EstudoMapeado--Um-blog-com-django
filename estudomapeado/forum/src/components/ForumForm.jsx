import React, { useState } from 'react';

const ForumForm = ({ onCommentSubmit }) => {
  const [newMessage, setNewMessage] = useState('');

  const handleFormSubmit = async event => {
    event.preventDefault();

    // Make a POST request to your API to add a new message
    try {
      const response = await fetch('http://127.0.0.1:8000/api/v1/forummessages/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: newMessage }),
      });

      // Handle the response as needed
      console.log('New message added:', response);

      // Notify the parent component (ForumPage) that a new comment has been added
      onCommentSubmit();
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
