import React, { useState } from "react";
import axios from "axios";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/auth/login", 
        new URLSearchParams({ username, password }),
        { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
      );
      onLogin(res.data.access_token);
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;
