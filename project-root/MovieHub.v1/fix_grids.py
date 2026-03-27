import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

# Let's target the exact text right before the grid end to append things.
# Romance
# In Horror: The Deadly Little Mermaid
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
              </article>
"""

# Replace in Horror section
horror_str = """          <div class="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
            <!-- Movie Card 1 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1596205804368-6f6eb5e925bf?auto=format&fit=crop&q=80&w=400" alt="Send Help" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">9.0</span>
                  <a href="https://www.youtube.com/watch?v=vVGe3XQ9Z-I" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    Send Help
                  </h3>
                  <p class="text-xs text-slate-300">Horror • 2018</p>
                </div>
              </div>
            </article>

            <!-- Movie Card 2 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1626297394663-125032b49520?auto=format&fit=crop&q=80&w=400" alt="The Deadly Little Mermaid" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.2</span>
                  <a href="https://www.youtube.com/watch?v=xU4bplQ2ZbY" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    The Deadly Little Mermaid
                  </h3>
                  <p class="text-xs text-slate-300">Horror • 2017</p>
                </div>
              </div>
            </article>
"""
if horror_str in content:
    content = content.replace(horror_str, horror_str + horror_append)
else:
    print("Could not find Horror section")


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
              </article>
"""

thriller_str = """          <div class="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
            <!-- Movie Card 1 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1549646429-2c7713d2a3ea?auto=format&fit=crop&q=80&w=400" alt="He Hit the Books" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.4</span>
                  <a href="https://www.youtube.com/watch?v=J_jluEktJvQ" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    He Hit the Books
                  </h3>
                  <p class="text-xs text-slate-300">Thriller • 2011</p>
                </div>
              </div>
            </article>

            <!-- Movie Card 2 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400" alt="Blood Drops" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">9.0</span>
                  <a href="https://www.youtube.com/watch?v=AFuE1LRxm80" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    Blood Drops
                  </h3>
                  <p class="text-xs text-slate-300">Thriller • 2000</p>
                </div>
              </div>
            </article>
"""

if thriller_str in content:
    content = content.replace(thriller_str, thriller_str + thriller_append)
else:
    print("Could not find Thriller section")

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
              </article>
"""

comedy_str = """          <div class="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
            <!-- Movie Card 1 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400" alt="I Miss The Mail" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.1</span>
                  <a href="https://www.youtube.com/watch?v=RkX-1rX6Wp4" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    I Miss The Mail
                  </h3>
                  <p class="text-xs text-slate-300">Comedy • 2004</p>
                </div>
              </div>
            </article>

            <!-- Movie Card 2 -->
            <article class="group relative flex aspect-[2/3] cursor-pointer flex-col justify-end overflow-hidden rounded-md transition-all duration-300 hover:scale-[1.02]">
              <img src="https://images.unsplash.com/photo-1563207436-b6ef028e08d6?auto=format&fit=crop&q=80&w=400" alt="Who's The Daddy?" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent"></div>
              <div class="relative flex h-full flex-col justify-between p-4">
                <div class="flex items-center justify-between">
                  <span class="rounded bg-black/40 px-2 py-0.5 text-xs font-medium text-white backdrop-blur-md">8.6</span>
                  <a href="https://www.youtube.com/watch?v=5-7eWDBc400" target="_blank" rel="noopener noreferrer" class="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white backdrop-blur-md transition-colors hover:bg-emerald-500 hover:text-white" aria-label="Play Trailer">
                    ▶
                  </a>
                </div>
                <div>
                  <h3 class="line-clamp-1 font-semibold text-white">
                    Who's The Daddy?
                  </h3>
                  <p class="text-xs text-slate-300">Comedy • 2011</p>
                </div>
              </div>
            </article>
"""

if comedy_str in content:
    content = content.replace(comedy_str, comedy_str + comedy_append)
else:
    print("Could not find Comedy section")

Path("static/index.html").write_text(content, encoding="utf-8")
print("Done")