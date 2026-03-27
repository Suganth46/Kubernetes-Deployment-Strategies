import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

# Let's fix the Horror section
horror_append = """              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/dzBootUD4I9T2nLdxyK17z0yFwE.jpg" alt="Get Out" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.1</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">Get Out</h3>
                    <p class="text-xs text-slate-300">Horror • 2017</p>
                  </div>
                </div>
              </article>
              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg" alt="A Quiet Place" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.1</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">A Quiet Place</h3>
                    <p class="text-xs text-slate-300">Horror • 2018</p>
                  </div>
                </div>
              </article>"""

# Using regex to find the end of the Deadly Little Mermaid block
content = re.sub(
    r'(<h3 class="line-clamp-1 font-semibold text-white">\s*The Deadly Little Mermaid\s*</h3>\s*<p class="text-xs text-slate-300">Horror • \d{4}</p>\s*</div>\s*</div>\s*</article>)',
    r'\1\n' + horror_append,
    content
)

thriller_append = """              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/69SsnCRQRVKgGlOUQqX9HQgNV9g.jpg" alt="Se7en" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.6</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">Se7en</h3>
                    <p class="text-xs text-slate-300">Thriller • 1995</p>
                  </div>
                </div>
              </article>
              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQIgTGvRv.jpg" alt="Inception" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.8</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">Inception</h3>
                    <p class="text-xs text-slate-300">Thriller • 2010</p>
                  </div>
                </div>
              </article>"""

content = re.sub(
    r'(<h3 class="line-clamp-1 font-semibold text-white">\s*Blood Drops\s*</h3>\s*<p class="text-xs text-slate-300">Thriller • \d{4}</p>\s*</div>\s*</div>\s*</article>)',
    r'\1\n' + thriller_append,
    content
)


comedy_append = """              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg" alt="Superbad" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">7.6</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">Superbad</h3>
                    <p class="text-xs text-slate-300">Comedy • 2007</p>
                  </div>
                </div>
              </article>
              <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
                <img src="https://image.tmdb.org/t/p/w500/yA33Fw1alBTAz32Gf2hT167I4vT.jpg" alt="Step Brothers" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
                <div class="relative flex h-full flex-col justify-between p-4">
                  <div class="flex items-center justify-between">
                    <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">7.0</span>
                    <button class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">▶</button>
                  </div>
                  <div>
                    <h3 class="line-clamp-1 font-semibold text-white">Step Brothers</h3>
                    <p class="text-xs text-slate-300">Comedy • 2008</p>
                  </div>
                </div>
              </article>"""

content = re.sub(
    r'(<h3 class="line-clamp-1 font-semibold text-white">\s*Who\'s The Daddy\?\s*</h3>\s*<p class="text-xs text-slate-300">Comedy • \d{4}</p>\s*</div>\s*</div>\s*</article>)',
    r'\1\n' + comedy_append,
    content
)

Path("static/index.html").write_text(content, encoding="utf-8")
print("All grids patched!")
