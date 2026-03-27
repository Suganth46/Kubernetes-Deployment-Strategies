import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import HeroSlider from './components/HeroSlider';
import MovieGrid from './components/MovieGrid';
import Login from './components/Login';
import AdminDashboard from './components/AdminDashboard';
import { getCurrentUser } from './utils/auth';

// A wrapper component to protect the home page
const ProtectedRoute = ({ children }) => {
  const user = getCurrentUser();
  if (!user) {
    return <Navigate to="/login" replace />;
  }
  return children;
};

// Application Main View
const Home = () => {
  return (
    <div className="app-container">
      <Navbar />
      <HeroSlider />
      <main className="main-content">
        <MovieGrid />
      </main>
    </div>
  );
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          } 
        />
        <Route 
          path="/admin" 
          element={
            <ProtectedRoute>
              <AdminDashboard />
            </ProtectedRoute>
          } 
        />
      </Routes>
    </Router>
  );
}

export default App;
