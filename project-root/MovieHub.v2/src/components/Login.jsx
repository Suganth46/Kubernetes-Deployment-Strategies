import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { login, initAuth } from '../utils/auth';
import { Film, User, Lock } from 'lucide-react';
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    initAuth();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    setError('');

    if (!email || !password) {
      setError('Please fill in all fields.');
      return;
    }

    const res = login(email, password);
    if (res.success) {
      navigate('/'); // Redirect to home on success
    } else {
      setError(res.message);
    }
  };

  return (
    <div className="login-container">
      <div className="login-card glass">
        <div className="login-header">
          <Film className="login-logo-icon" size={40} />
          <h2>Welcome to Sofa Cinema</h2>
          <p>Login or register to access the movies</p>
        </div>

        {error && <div className="login-error">{error}</div>}

        <form onSubmit={handleSubmit} className="login-form">
          <div className="input-group">
            <User className="input-icon" size={20} />
            <input 
              type="email" 
              placeholder="Email address" 
              className="login-input"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="input-group">
            <Lock className="input-icon" size={20} />
            <input 
              type="password" 
              placeholder="Password" 
              className="login-input"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="login-btn">
            Enter
          </button>
        </form>
        
        <p className="login-hint">If your email is new, an account will be automatically registered.</p>
      </div>
    </div>
  );
};

export default Login;
