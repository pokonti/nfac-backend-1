import { useState } from 'react';
import './App.css'
import Projects from './components/Projects';
import Login from './components/Login';

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  const handleLogin = (token) => {
    localStorage.setItem("token", token);
    setToken(token);
  };

  return token ? (
    <Projects token={token} />
  ) : (
    <Login onLogin={handleLogin} />
  );
}

export default App
