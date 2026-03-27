const getYear = (dateValue) => dateValue.split("-")[0];

export default function ImdbTop({ list, showNoResults = false }) {
  const hasResults = list && list.length > 0;

  return (
    <section className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-semibold text-white">IMDb Top Ranked</h2>
          <p className="text-sm text-slate-300">
            Timeless picks with legendary ratings.
          </p>
        </div>
        <button className="rounded-full border border-white/15 px-4 py-2 text-xs uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10">
          View full list
        </button>
      </div>

      {showNoResults && !hasResults ? (
        <div className="rounded-2xl border border-white/10 bg-white/5 px-6 py-4 text-sm text-slate-200">
          No results found. Try a different search or clear filters.
        </div>
      ) : null}

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {(list || []).map((movie) => (
          <article
            key={movie.id}
            className="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40"
            data-year={getYear(movie.releaseDate)}
            data-title={movie.title.toLowerCase()}
            data-genre={movie.genre.toLowerCase()}
          >
            <div className="relative">
              <img
                src={movie.poster}
                alt={movie.title}
                className="h-56 w-full object-cover transition duration-500 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent" />
              <span className="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                {movie.genre}
              </span>
            </div>
            <div className="flex flex-1 flex-col gap-4 p-5">
              <div className="space-y-2">
                <h3 className="text-lg font-semibold text-white">
                  {movie.title}
                </h3>
                <p className="text-sm text-slate-300">{movie.overview}</p>
              </div>
              <div className="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                <span>{getYear(movie.releaseDate)}</span>
                <span>Rating {movie.rating}</span>
              </div>
              <a
                className="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                href={movie.trailerUrl}
                target="_blank"
                rel="noreferrer"
              >
                Watch trailer
              </a>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
