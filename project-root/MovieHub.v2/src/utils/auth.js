// auth.js - handles local storage simulation of a database

const ADMIN_EMAIL = 'selvamthiru712@gmail.com';
const ADMIN_PASS = '_Thiru@4690';

export const initAuth = () => {
  // Initialize users array if it doesn't exist
  if (!localStorage.getItem('users')) {
    localStorage.setItem('users', JSON.stringify([]));
  }
};

export const login = (email, password) => {
  if (email === ADMIN_EMAIL && password === ADMIN_PASS) {
    const adminUser = { email, isAdmin: true };
    localStorage.setItem('currentUser', JSON.stringify(adminUser));
    return { success: true, user: adminUser };
  }

  // Check if exists as normal user
  const users = JSON.parse(localStorage.getItem('users') || '[]');
  const user = users.find(u => u.email === email);
  
  if (user) {
    if (user.password === password) {
      const normalUser = { email, isAdmin: false };
      localStorage.setItem('currentUser', JSON.stringify(normalUser));
      return { success: true, user: normalUser };
    } else {
      return { success: false, message: 'Invalid credentials. Incorrect password.' };
    }
  }

  // Auto-register if user doesn't exist (as per simple "login" requests to just enter)
  // Usually this would be a separate register page, but for simplicity, we create the account if it doesn't exist.
  users.push({ email, password });
  localStorage.setItem('users', JSON.stringify(users));
  
  const newUser = { email, isAdmin: false };
  localStorage.setItem('currentUser', JSON.stringify(newUser));
  return { success: true, user: newUser, message: 'Account registered and logged in.' };
};

export const logout = () => {
  localStorage.removeItem('currentUser');
};

export const getCurrentUser = () => {
  const user = localStorage.getItem('currentUser');
  return user ? JSON.parse(user) : null;
};

export const getAllUsers = () => {
  return JSON.parse(localStorage.getItem('users') || '[]');
};
