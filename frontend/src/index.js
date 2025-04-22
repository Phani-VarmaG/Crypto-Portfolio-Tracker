// Import React for rendering components.
import React from 'react';
// Import ReactDOM for interacting with the DOM.
import ReactDOM from 'react-dom/client';
// Import the main App component.
import App from './App';

// Create a root element for the React application.
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // Enable additional checks and warnings in development mode.
  <React.StrictMode>
    <App />
  </React.StrictMode>
);