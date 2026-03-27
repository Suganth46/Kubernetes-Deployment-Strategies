import React from 'react';
import { Search, Film, UserCircle, LogOut, Shield } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { getCurrentUser, logout } from '../utils/auth';
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate();
  const user = getCurrentUser();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar glass">
      <div className="navbar-container">
        <div 
          className="navbar-logo" 
          onClick={() => navigate('/')}
          style={{ cursor: 'pointer' }}
        >
          <Film className="logo-icon" />
          <span>SofaCinema</span>
        </div>

        <div className="navbar-menus">
          
          {user && user.isAdmin && (
            <button className="nav-btn admin-badge" onClick={() => navigate('/admin')}>
              <Shield size={16} /> Admin
            </button>
          )}

          {user && (
            <div className="user-profile">
              <UserCircle size={20} className="profile-icon" />
              <span className="profile-email">{user.email.split('@')[0]}</span>
            </div>
          )}

          <button className="nav-btn logout-btn" onClick={handleLogout} title="Logout">
            <LogOut size={18} />
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
