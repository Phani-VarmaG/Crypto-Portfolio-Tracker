// Import React and the useState hook to manage component state.
import React, { useState } from 'react';
// Import the login service function to handle authentication.
import { login } from '../services/auth';
// Import useNavigate to programmatically change routes.
import { useNavigate } from 'react-router-dom';

const Login = () => {
  // State variable for storing the email input.
  const [email, setEmail] = useState('');
  // State variable for storing the password input.
  const [password, setPassword] = useState('');
  // Hook to navigate after a successful login.
  const navigate = useNavigate();

  // This function is called when the login form is submitted.
  const handleSubmit = async e => {
    // Prevent the default form submission behavior.
    e.preventDefault();
    try {
      // Call the login service to authenticate the user.
      const data = await login(email, password);
      // If authentication token is returned, navigate to the home page.
      if (data.token) {
        navigate('/');
      }
    } catch (error) {
      // If login fails, alert the user.
      alert('Login failed');
    }
  };

  // Render the login form.
  return (
    <div>
      <h2>Login</h2>
      {/* Form to capture email and password */}
      <form onSubmit={handleSubmit}>
        <input 
          type="email" 
          placeholder="Email" 
          value={email}
          onChange={e => setEmail(e.target.value)} 
          required 
        />
        <input 
          type="password" 
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)} 
          required 
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;