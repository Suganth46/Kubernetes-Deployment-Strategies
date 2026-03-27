import re

with open("static/index.html", "r", encoding="utf-8") as f:
    text = f.read()

romance_html = """
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/qJeU7KM4nT2C1WpOrwPcSDGFUWE.jpg"
                        alt="La La Land"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Romance Musical
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">La La Land</h4>
                        <p class="text-sm text-slate-300">
                          Mia and Sebastian are struggling to make ends meet in a city known for crushing hopes.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2016-12-29</span>
                        <span>Rating 8.0</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=0pdqf4P9MB8"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/qom1SZRENs404DnghMvD2hLzUo9.jpg"
                        alt="The Notebook"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Romance Drama
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">The Notebook</h4>
                        <p class="text-sm text-slate-300">
                          An epic love story centered around an older man who reads aloud to a woman.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2004-06-25</span>
                        <span>Rating 7.9</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=FC6biTjEyZw"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>"""

horror_html = """
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/7bSQ2WihNIVaZ0E7Btv440rN8rV.jpg"
                        alt="Get Out"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Horror Thriller
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">Get Out</h4>
                        <p class="text-sm text-slate-300">
                          Chris uncovers a disturbing secret at his girlfriend's parents' estate.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2017-02-24</span>
                        <span>Rating 7.6</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=DzfpyUB60YY"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/roYyPiQmuvnLSFw1I3k9sFq1K12.jpg"
                        alt="A Quiet Place"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Horror Drama
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">A Quiet Place</h4>
                        <p class="text-sm text-slate-300">
                          A family is forced to live in silence while hiding from creatures that hunt by sound.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2018-04-06</span>
                        <span>Rating 7.6</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=WR7cc5t7tv8"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>"""

thriller_html = """
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/2yFqQ8IivvI1t4lO1fXyAmlZzEY.jpg"
                        alt="Se7en"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Crime Thriller
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">Se7en</h4>
                        <p class="text-sm text-slate-300">
                          Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>1995-09-22</span>
                        <span>Rating 8.6</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=znmZoVkCjpI"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/ztZ4vw151mw04Bg6rqJLQGAA40Z.jpg"
                        alt="Inception"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Action Thriller
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">Inception</h4>
                        <p class="text-sm text-slate-300">
                          A thief who steals corporate secrets through the use of dream-sharing technology.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2010-07-16</span>
                        <span>Rating 8.8</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=YoHD9XEInc0"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>"""

comedy_html = """
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/dO3HjXv40129gM6e7r7vV2f6FvI.jpg"
                        alt="Superbad"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Comedy
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">Superbad</h4>
                        <p class="text-sm text-slate-300">
                          Two co-dependent high school seniors plan to stage a booze-soaked party.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2007-08-17</span>
                        <span>Rating 7.3</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=MN8fVMcHLew"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>
                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="https://image.tmdb.org/t/p/w780/2qH6w7Kk7t6K3YhM7JXVm08gHkG.jpg"
                        alt="Step Brothers"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        Comedy
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">Step Brothers</h4>
                        <p class="text-sm text-slate-300">
                          Two aimless middle-aged losers are forced to become room-mates.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>2008-07-25</span>
                        <span>Rating 7.1</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="https://www.youtube.com/watch?v=CewglxElBK0"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>"""

text = re.sub(r'(href="https://www\.youtube\.com/watch\?v=3fLCdIYShEQ"[^>]*>\s*Watch trailer\s*</a>\s*</div>\s*</article>)', "\\1\n" + romance_html, text)
text = re.sub(r'(href="https://www\.youtube\.com/watch\?v=1ZWe3i3xS0Y"[^>]*>\s*Watch trailer\s*</a>\s*</div>\s*</article>)', "\\1\n" + horror_html, text)
text = re.sub(r'(href="https://www\.youtube\.com/watch\?v=_QeL9N733yA"[^>]*>\s*Watch trailer\s*</a>\s*</div>\s*</article>)', "\\1\n" + thriller_html, text)
text = re.sub(r'(href="https://www\.youtube\.com/watch\?v=1v_H1lK-3jE"[^>]*>\s*Watch trailer\s*</a>\s*</div>\s*</article>)', "\\1\n" + comedy_html, text)

with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Done index.html Update.")