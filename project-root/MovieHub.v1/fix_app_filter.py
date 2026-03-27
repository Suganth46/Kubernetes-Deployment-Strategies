import re
from pathlib import Path

content = Path("src/App.jsx").read_text(encoding="utf-8")

old_filteredImdb = """  const filteredImdb = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();

    return imdbTop.filter((movie) => {
      const movieYear = movie.releaseDate.split("-")[0];
      const matchesSearch =
        !normalizedSearch ||
        movie.title.toLowerCase().includes(normalizedSearch) ||
        movie.genre.toLowerCase().includes(normalizedSearch) ||
        movieYear.includes(normalizedSearch);

      const matchesGenre =
        !activeGenre || movie.genre.toLowerCase().includes(activeGenre);

      return matchesSearch && matchesGenre;
    });
  }, [search, activeGenre]);"""

new_filteredImdb = """  const filteredImdb = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();

    return imdbTop.filter((movie) => {
      const movieYear = movie.releaseDate.split("-")[0];
      const matchesSearch =
        !normalizedSearch ||
        movie.title.toLowerCase().includes(normalizedSearch) ||
        movie.genre.toLowerCase().includes(normalizedSearch) ||
        movieYear.includes(normalizedSearch);

      const matchesGenre =
        !activeGenre || movie.genre.toLowerCase().includes(activeGenre);

      return matchesSearch && matchesGenre;
    });
  }, [search, activeGenre]);

  const filteredGenreSections = useMemo(() => {
    const normalizedSearch = search.trim().toLowerCase();
    
    return genreSections.map(section => {
      const filteredMovies = section.movies.filter(movie => {
        const movieYear = movie.releaseDate.split("-")[0];
        const matchesSearch =
          !normalizedSearch ||
          movie.title.toLowerCase().includes(normalizedSearch) ||
          movie.genre.toLowerCase().includes(normalizedSearch) ||
          movieYear.includes(normalizedSearch);
          
        const matchesGenre =
          !activeGenre ||
          movie.genre.toLowerCase().includes(activeGenre) ||
          section.title.toLowerCase().includes(activeGenre);

        return matchesSearch && matchesGenre;
      });
      return {
        ...section,
        movies: filteredMovies
      };
    }).filter(section => section.movies.length > 0);
  }, [search, activeGenre]);"""

content = content.replace(old_filteredImdb, new_filteredImdb)

content = content.replace(
    "<GenreShowcase\n              sections={genreSections}",
    "<GenreShowcase\n              sections={filteredGenreSections}"
)

Path("src/App.jsx").write_text(content, encoding="utf-8")
print("Done styling App.jsx")
