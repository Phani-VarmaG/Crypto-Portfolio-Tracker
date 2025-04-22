// Import React and useState hook for managing local state.
import React, { useState } from 'react';

const Settings = () => {
  // State variable for username input.
  const [username, setUsername] = useState('');
  // State variable for email input.
  const [email, setEmail] = useState('');

  // Function to handle form submission for updating settings.
  const handleUpdate = (e) => {
    // Prevent default form submission.
    e.preventDefault();
    // TODO: Implement settings update functionality (e.g., API call).
    // Display an alert with the updated username.
    alert(`Updated settings for ${username}`);
  };

  // Render a form to update user settings.
  return (
    <div>
      <h2>User Settings</h2>
      <form onSubmit={handleUpdate}>
        <input 
          type="text"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />
        <input 
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <button type="submit">Update Settings</button>
      </form>
    </div>
  );
};

export default Settings;