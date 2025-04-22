// Import React for component creation.
import React from 'react';
// Import routing components from react-router-dom.
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// Import page components for routing.
import Portfolio from './pages/Portfolio';
import Login from './pages/Login';
import Settings from './pages/Settings';

const App = () => {
  return (
    // Wrap the application in a router for navigation.
    <Router>
      <Routes>
        {/* Route for the portfolio dashboard */}
        <Route path="/" element={<Portfolio />} />
        {/* Route for the login page */}
        <Route path="/login" element={<Login />} />
        {/* Route for the settings page */}
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Router>
  );
};

export default App;
