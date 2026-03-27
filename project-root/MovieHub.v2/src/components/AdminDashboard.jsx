import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCurrentUser, getAllUsers } from '../utils/auth';
import { Users, ShieldAlert, ArrowLeft } from 'lucide-react';
import './AdminDashboard.css';

const AdminDashboard = () => {
  const [users, setUsers] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const user = getCurrentUser();
    if (!user || user.email !== 'selvamthiru712@gmail.com') {
      navigate('/login'); // Not an admin
    } else {
      setCurrentUser(user);
      setUsers(getAllUsers());
    }
  }, [navigate]);

  if (!currentUser) return null;

  return (
    <div className="admin-dashboard-container">
      <div className="admin-header glass">
        <button className="back-btn" onClick={() => navigate('/')}>
          <ArrowLeft size={20} /> Back to Movies
        </button>
        <div className="admin-title">
          <ShieldAlert size={24} className="admin-icon" />
          <h2>Admin Dashboard</h2>
        </div>
      </div>

      <div className="admin-content glass">
        <div className="admin-content-header">
          <h3><Users className="users-icon" /> Registered User Accounts</h3>
          <span className="user-count">{users.length} total</span>
        </div>

        <div className="admin-table-container">
          {users.length === 0 ? (
            <div className="no-users">No users have registered yet.</div>
          ) : (
            <table className="admin-table">
              <thead>
                <tr>
                  <th>No.</th>
                  <th>Email Address</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {users.map((u, idx) => (
                  <tr key={idx}>
                    <td>{idx + 1}</td>
                    <td>{u.email}</td>
                    <td><span className="status-badge">Active</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
