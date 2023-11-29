import React, { useEffect, useState } from 'react';
import ForumMessage from './ForumMessage'; // Assuming you'll create this component

const ForumList = () => {
  const [forumMessages, setForumMessages] = useState([]);

  useEffect(() => {
    // Fetch data from the API when the component mounts
    const fetchForumMessages = async () => {
      try {
        const response = await fetch('http://your-api-url/api/v1/forummessages/');
        const data = await response.json();
        setForumMessages(data);
      } catch (error) {
        console.error('Error fetching forum messages:', error);
      }
    };

    fetchForumMessages();
  }, []);

  return (
    <div>
      {/* Render the forum messages using the state */}
      {forumMessages.map(message => (
        <ForumMessage key={message.id} message={message} />
      ))}
    </div>
  );
};

export default ForumList;
