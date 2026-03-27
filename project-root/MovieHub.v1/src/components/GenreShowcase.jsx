export default function GenreShowcase({ sections, onExplore }) {
  if (!sections || sections.length === 0) {
    return null;
  }

  return (
    <section className="space-y-10">
      <div>
        <h2 className="text-2xl font-semibold text-white">Genre Radar</h2>
        <p className="text-sm text-slate-300">
          Curated picks across every mood.
        </p>
      </div>

      <div className="grid gap-8">
        {sections.map((section) => (
          <div key={section.key} className="space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div>
                <h3 className="text-xl font-semibold text-white">
                  {section.title}
                </h3>
                <p className="text-sm text-slate-300">{section.description}</p>
              </div>
              <button
                className="rounded-full border border-white/15 px-4 py-2 text-xs uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                type="button"
                onClick={() => onExplore?.(section.key)}
              >
                Explore {section.title}
              </button>
            </div>
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {section.movies.map((movie) => (
                <article
                  key={movie.id}
                  className="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40"
                >
                  <div className="relative">
                    <img
                      src={movie.backdrop}
                      alt={movie.title}
                      className="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent" />
                    <span className="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                      {movie.genre}
                    </span>
                  </div>
                  <div className="flex flex-1 flex-col gap-4 p-5">
                    <div className="space-y-2">
                      <h4 className="text-lg font-semibold text-white">
                        {movie.title}
                      </h4>
                      <p className="text-sm text-slate-300">{movie.overview}</p>
                    </div>
                    <div className="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                      <span>{movie.releaseDate}</span>
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
          </div>
        ))}
      </div>
    </section>
  );
}
