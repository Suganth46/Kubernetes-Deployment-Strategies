import React, { useState } from 'react';
import { Star, Tv2, Calendar, Play } from 'lucide-react';
import './MovieCard.css';

const MovieCard = ({ movie, onSelect }) => {
  const [isHovered, setIsHovered] = useState(false);

  const fallbackImage = "https://images.unsplash.com/photo-1542204165-65bf26472b9b?q=80&w=800&auto=format&fit=crop";

  return (
    <div 
      className="movie-card"
      onClick={() => onSelect(movie)}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      title="Click for details"
    >
      <div className="card-image-container">
        <img 
          src={movie.poster} 
          alt={movie.title} 
          className="card-image"
          loading="lazy"
          onError={(e) => { e.target.src = fallbackImage; }}
        />
        
        {isHovered && (
          <div className="play-overlay animate-fade-in">
            <span style={{color: '#fff', background: 'rgba(0,0,0,0.6)', padding:'8px 16px', borderRadius:'20px', fontSize:'0.9rem', fontWeight:'600'}}>View Details</span>
          </div>
        )}
      </div>

      <div className={`card-content ${isHovered ? 'hovered' : ''}`}>
        <h3 className="card-title">{movie.title}</h3>
        
        <div className="card-meta">
          <span className="meta-item">
            <Star size={14} className="star-icon" fill="currentColor" />
            {movie.rating}
          </span>
          <span className="meta-item">{movie.genre}</span>
          <span className="meta-item">{movie.language}</span>
        </div>

        <div className="card-details">
          <p className="card-description">{movie.description}</p>
        </div>
      </div>
    </div>
  );
};

export default MovieCard;
