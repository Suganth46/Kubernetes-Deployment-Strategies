import { useMemo, useState } from "react";
import { genreSections, imdbTop, nowPlaying } from "./data/movies";
import Hero from "./components/Hero";
import RecentlyReleased from "./components/RecentlyReleased";
import GenreShowcase from "./components/GenreShowcase";
import ImdbTop from "./components/ImdbTop";
import Newsletter from "./components/Newsletter";
import Footer from "./components/Footer";
import "./index.css";

export default function App() {
  const [search, setSearch] = useState("");
  const [activeGenre, setActiveGenre] = useState("");

  const filteredImdb = useMemo(() => {
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

  const hasFilters = Boolean(search.trim() || activeGenre);

  const recentMovies = nowPlaying.slice(1);

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="relative">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(16,185,129,0.12),transparent_55%)]" />
        <div className="absolute inset-0 bg-[linear-gradient(120deg,rgba(15,23,42,0.95),rgba(15,23,42,0.75),rgba(15,23,42,0.95))]" />
        <div className="relative mx-auto flex max-w-6xl flex-col gap-12 px-6 py-12 md:py-16">
          <header className="flex flex-wrap items-center justify-between gap-6">
            <div>
              <p className="text-xs uppercase tracking-[0.3em] text-emerald-200">
                MovieHub v1
              </p>
              <h1 className="text-2xl font-semibold text-white">
                Original Hollywood Archive
              </h1>
            </div>
            <nav className="flex flex-wrap gap-4 text-xs uppercase tracking-[0.2em] text-slate-300">
              <a className="transition hover:text-white" href="#">
                Reviews
              </a>
              <a className="transition hover:text-white" href="#">
                Watchlists
              </a>
              <a className="transition hover:text-white" href="#">
                Editorial
              </a>
            </nav>
          </header>

          

          <Hero movies={nowPlaying} />
          <RecentlyReleased list={recentMovies} />
          <GenreShowcase
            sections={genreSections}
            onExplore={(genreKey) => setActiveGenre(genreKey)}
          />
          <ImdbTop list={filteredImdb} showNoResults={hasFilters} />
          <Newsletter />
          <Footer />
        </div>
      </div>
    </div>
  );
}
