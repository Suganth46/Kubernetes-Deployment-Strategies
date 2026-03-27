export default function Featured({ movie }) {
  if (!movie) {
    return null;
  }

  return (
    <section className="grid gap-8 rounded-3xl border border-white/10 bg-gradient-to-br from-slate-900/80 via-slate-950 to-slate-950 px-8 py-10 md:grid-cols-[0.9fr_1.1fr] md:px-12">
      <div className="order-2 space-y-5 md:order-1">
        <p className="text-xs uppercase tracking-[0.3em] text-emerald-200">
          Spotlight Review
        </p>
        <h2 className="text-3xl font-semibold text-white md:text-4xl">
          {movie.title}
        </h2>
        <p className="text-slate-200/90">{movie.blurb}</p>
        <div className="flex flex-wrap gap-3 text-sm text-slate-300">
          <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
            {movie.genre}
          </span>
          <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
            {movie.runtime}
          </span>
          <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
            {movie.certificate}
          </span>
          <span className="rounded-full border border-white/15 bg-white/5 px-4 py-2">
            Rating {movie.rating}
          </span>
        </div>
        <div className="flex flex-wrap gap-4">
          <button className="rounded-full border border-emerald-200/60 px-6 py-3 text-sm font-semibold text-emerald-100 transition hover:bg-emerald-200 hover:text-slate-900">
            Full critique
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

      <div className="order-1 md:order-2">
        <div className="relative overflow-hidden rounded-2xl border border-white/10">
          <img
            src={movie.backdrop}
            alt={movie.title}
            className="h-full w-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent" />
          <div className="absolute bottom-4 left-4 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs uppercase tracking-[0.2em] text-white">
            {movie.year}
          </div>
        </div>
      </div>
    </section>
  );
}
