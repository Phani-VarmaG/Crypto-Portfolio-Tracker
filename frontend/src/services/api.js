// This file creates and configures an Axios instance to interact with the backend API.
import axios from 'axios';

// Create an Axios instance with a base URL.
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000',
});

// Interceptor to inject the JWT token in every request header if available.
api.interceptors.request.use(config => {
  // Retrieve the token from local storage.
  const token = localStorage.getItem('token');
  if (token) {
    // Attach the token to the x-access-token header.
    config.headers['x-access-token'] = token;
  }
  return config;
});

export default api;
