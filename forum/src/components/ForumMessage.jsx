import React from 'react';

const ForumMessage = ({ message }) => {
  return (
    <div>
      <p>{message.user.username}</p>
      <p>{message.message}</p>
      {/* Add other message details as needed */}
    </div>
  );
};

export default ForumMessage;
