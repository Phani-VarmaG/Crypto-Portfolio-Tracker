export const login = async (email, password) => {
    const response = await api.post('/login', { email, password });
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
    }
    return response.data;
  };
  
  export const register = async (username, email, password) => {
    return api.post('/register', { username, email, password });
  };
  
  export const logout = () => {
    localStorage.removeItem('token');
  };
  