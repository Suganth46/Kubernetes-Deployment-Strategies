import { useEffect, useState } from "react";

export default function Hero({ movies }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    if (!movies || movies.length <= 1) return;
    const interval = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % movies.length);
    }, 5000);
    return () => clearInterval(interval);
  }, [movies]);

  if (!movies || movies.length === 0) {
    return null;
  }

  const movie = movies[currentIndex];

  return (
    <section className="relative overflow-hidden rounded-3xl border border-white/10 bg-slate-950/70 shadow-[0_30px_80px_-50px_rgba(15,23,42,0.9)] transition-all duration-700">
      <div key={movie.id} className="animate-fade">
        <div className="absolute inset-0">
          <img
            src={movie.backdrop}
            alt={movie.title}
            className="h-full w-full object-cover opacity-70 transition-opacity duration-1000"
          />
          <div className="absolute inset-0 bg-gradient-to-br from-slate-950 via-slate-950/70 to-transparent" />
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_20%,rgba(94,234,212,0.2),transparent_45%)]" />
          <div className="grain absolute inset-0" />
        </div>

        <div className="relative z-10 grid gap-10 px-8 py-14 md:grid-cols-[1.1fr_0.9fr] md:px-14">
          <div className="space-y-6">
            <div className="inline-flex items-center gap-3 rounded-full border border-white/15 bg-white/5 px-4 py-2 text-xs uppercase tracking-[0.2em] text-emerald-200">
              Freshly Released
            </div>
            <h1 className="text-balance text-4xl font-semibold text-white md:text-6xl drop-shadow-lg">
              {movie.title}
            </h1>
            <p className="max-w-xl text-lg text-slate-200/90">
              {movie.overview}
            </p>
            <div className="flex flex-wrap gap-3 text-sm text-slate-300">
              <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
                {movie.genre}
              </span>
              <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
                {movie.releaseDate}
              </span>
              <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
                Rating {movie.rating}
              </span>
            </div>
            <div className="flex flex-wrap gap-4">
              <button className="shine rounded-full bg-emerald-300 px-6 py-3 text-sm font-semibold text-slate-900 transition hover:-translate-y-0.5">
                Read the review
              </button>
              <a
                className="rounded-full border border-white/20 px-6 py-3 text-sm font-semibold text-white transition hover:border-white/40 hover:bg-white/10"
                href={movie.trailerUrl}
                target="_blank"
                rel="noreferrer"
              >
                Watch trailer
              </a>
            </div>
          </div>

          <div className="relative">
            <div className="floating absolute -right-6 top-6 hidden h-24 w-24 rounded-full bg-emerald-200/20 blur-2xl md:block" />
            <div className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur">
              <img
                src={movie.poster}
                alt={movie.title}
                className="h-full w-full rounded-xl object-cover"
              />
              <div className="mt-4 flex items-center justify-between text-xs uppercase tracking-[0.2em] text-slate-300">
                <span>Now Playing</span>
                <span>{movie.releaseDate}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      {movies.length > 1 && (
        <div className="absolute bottom-6 left-0 right-0 flex justify-center gap-2 z-20">
          {movies.map((_, idx) => (
            <button
              key={idx}
              onClick={() => setCurrentIndex(idx)}
              className={`h-1.5 rounded-full transition-all ${idx === currentIndex ? 'bg-emerald-300 w-6' : 'bg-white/30 w-1.5 hover:bg-white/50'}`}
              aria-label={`Go to slide ${idx + 1}`}
            />
          ))}
        </div>
      )}
    </section>
  );
}
