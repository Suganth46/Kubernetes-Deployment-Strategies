import React, { useState } from 'react';
import { movies, genres, languages } from '../data';
import MovieCard from './MovieCard';
import MovieModal from './MovieModal';
import { Filter } from 'lucide-react';
import './MovieGrid.css';

const MovieGrid = () => {
  const [selectedGenre, setSelectedGenre] = useState('All');
  const [selectedLanguage, setSelectedLanguage] = useState('All');
  const [selectedMovie, setSelectedMovie] = useState(null);

  // Filter logic
  const filteredMovies = movies.filter(movie => {
    const genreMatch = selectedGenre === 'All' || movie.genre === selectedGenre;
    const languageMatch = selectedLanguage === 'All' || movie.language === selectedLanguage;
    return genreMatch && languageMatch;
  });

  return (
    <section className="catalog-section" id="catalog">
      <div className="catalog-header">
        <h2 className="section-title">Explore Movies</h2>
        
        <div className="filter-bar glass">
          <div className="filter-icon">
            <Filter size={20} />
            <span>Filters</span>
          </div>
          
          <div className="filter-group">
            <label htmlFor="genre-select">Genre:</label>
            <select 
              id="genre-select" 
              className="filter-select"
              value={selectedGenre}
              onChange={(e) => setSelectedGenre(e.target.value)}
            >
              {genres.map(genre => (
                <option key={genre} value={genre}>{genre}</option>
              ))}
            </select>
          </div>

          <div className="filter-group">
            <label htmlFor="lang-select">Language:</label>
            <select 
              id="lang-select" 
              className="filter-select"
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value)}
            >
              {languages.map(lang => (
                <option key={lang} value={lang}>{lang}</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      <div className="movies-grid animate-fade-in" style={{ animationDelay: '0.4s' }}>
        {filteredMovies.length > 0 ? (
          filteredMovies.map(movie => (
            <MovieCard 
              key={movie.id} 
              movie={movie} 
              onSelect={setSelectedMovie} 
            />
          ))
        ) : (
          <div className="no-results">
            <p>No movies found matching your criteria.</p>
            <button 
              className="btn-clear glass"
              onClick={() => {
                setSelectedGenre('All');
                setSelectedLanguage('All');
              }}
            >
              Clear Filters
            </button>
          </div>
        )}
      </div>

      {/* Renders modal if selectedMovie is not null */}
      <MovieModal 
        movie={selectedMovie} 
        onClose={() => setSelectedMovie(null)} 
      />
    </section>
  );
};

export default MovieGrid;
