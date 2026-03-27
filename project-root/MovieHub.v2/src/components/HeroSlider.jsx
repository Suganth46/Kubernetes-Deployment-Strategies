import React, { useState, useEffect } from 'react';
import { newReleases } from '../data';
import { Play, Info } from 'lucide-react';
import './HeroSlider.css';

const HeroSlider = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % newReleases.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="hero-slider">
      {newReleases.map((movie, index) => (
        <div
          key={movie.id}
          className={`hero-slide ${index === currentIndex ? 'active' : ''}`}
        >
          <div className="hero-background-wrapper">
            <img 
              src={movie.widePoster || movie.poster} 
              alt={movie.title} 
              className="hero-background" 
            />
            <div className="hero-gradient-overlay"></div>
          </div>
          
          <div className="hero-content">
            <div className="hero-tags animate-slide-up">
              <span className="glass-pill glass">New Release</span>
              <span className="hero-rating">{movie.rating} rating</span>
            </div>
            
            <h1 className="hero-title animate-slide-up" style={{ animationDelay: '0.1s' }}>
              {movie.title}
            </h1>
            
            <p className="hero-description animate-slide-up" style={{ animationDelay: '0.2s' }}>
              {movie.description}
            </p>
            
            <div className="hero-actions animate-slide-up" style={{ animationDelay: '0.3s' }}>
              <button className="btn-primary">
                <Play fill="currentColor" size={20} />
                Watch Trailer
              </button>
              <button className="btn-secondary glass">
                <Info size={20} />
                More Info
              </button>
            </div>
          </div>
        </div>
      ))}
      
      <div className="slider-indicators">
        {newReleases.map((_, index) => (
          <button
            key={index}
            className={`indicator ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

export default HeroSlider;
