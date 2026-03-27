import React, { useEffect } from 'react';
import { X, Play, Star, Users } from 'lucide-react';
import './MovieModal.css';

const MovieModal = ({ movie, onClose }) => {
  if (!movie) return null;

  return (
    <div className="modal-overlay animate-fade-in" onClick={onClose}>
      <div 
        className="modal-content animate-slide-up" 
        onClick={(e) => e.stopPropagation()} // Prevent click from bubbling to overlay
      >
        <button className="modal-close" onClick={onClose} aria-label="Close modal">
          <X size={24} />
        </button>

        <div className="modal-grid">
          <div className="modal-poster-wrapper">
            <img 
              src={movie.poster} 
              alt={movie.title} 
              className="modal-poster"
              onError={(e) => { e.target.src = "https://images.unsplash.com/photo-1542204165-65bf26472b9b?q=80&w=800&auto=format&fit=crop"; }}
            />
          </div>
          
          <div className="modal-info">
            <h2 className="modal-title">{movie.title}</h2>
            
            <div className="modal-meta">
              <span className="meta-tag"><Star size={14} className="star-icon" fill="currentColor"/> {movie.rating}</span>
              <span className="meta-tag">{movie.genre}</span>
              <span className="meta-tag">{movie.language}</span>
            </div>
            
            <p className="modal-description">{movie.description}</p>
            
            <div className="modal-cast-section">
              <h3 className="section-label">
                <Users size={16} /> Cast
              </h3>
              <ul className="cast-list">
                {movie.cast && movie.cast.map((actor, idx) => (
                  <li key={idx} className="cast-item">{actor}</li>
                ))}
              </ul>
            </div>
            
            <div className="modal-actions">
              <a 
                href={movie.trailerLink} 
                target="_blank" 
                rel="noopener noreferrer"
                className="btn-primary"
              >
                <Play fill="currentColor" size={20} />
                Watch Trailer
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MovieModal;
