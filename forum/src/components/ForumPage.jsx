import React, { useState } from 'react';
import ForumList from './ForumList';
import ForumForm from './ForumForm';

const ForumPage = () => {
  const [commentAdded, setCommentAdded] = useState(false);

  const handleCommentSubmit = () => {
    // Notify this component that a new comment has been added
    setCommentAdded(true);
  };

  return (
    <div>
      <h1>Forum Page</h1>
      <ForumList />
      <ForumForm onCommentSubmit={handleCommentSubmit} />
    </div>
  );
};

export default ForumPage;
