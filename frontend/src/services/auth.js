// This file provides authentication service functions for login, register, and logout.
import api from './api';
export const login = async (email, password) => {
  // Send a POST request to the backend /login endpoint
  const response = await api.post('/login', { email, password });
  // If a token is received, store it locally for future requests.
  if (response.data.token) {
    localStorage.setItem('token', response.data.token);
  }
  return response.data;
};

export const register = async (username, email, password) => {
  // Send a POST request to the backend /register endpoint with new user data.
  return api.post('/register', { username, email, password });
};

export const logout = () => {
  // Remove the token from local storage to log the user out.
  localStorage.removeItem('token');
};
