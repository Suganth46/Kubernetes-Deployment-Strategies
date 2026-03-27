import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

def make_card(title, release_date, rating, genre, image, trailer):
    return f"""                  <article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40">
                    <div class="relative">
                      <img
                        src="{image}"
                        alt="{title}"
                        class="h-48 w-full object-cover transition duration-500 group-hover:scale-105"
                      />
                      <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent"></div>
                      <span class="absolute left-4 top-4 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white">
                        {genre}
                      </span>
                    </div>
                    <div class="flex flex-1 flex-col gap-4 p-5">
                      <div class="space-y-2">
                        <h4 class="text-lg font-semibold text-white">{title}</h4>
                        <p class="text-sm text-slate-300">
                          Classic must-watch movie.
                        </p>
                      </div>
                      <div class="mt-auto flex flex-wrap items-center justify-between gap-3 text-xs uppercase tracking-[0.2em] text-slate-400">
                        <span>{release_date}</span>
                        <span>Rating {rating}</span>
                      </div>
                      <a
                        class="mt-2 inline-flex items-center justify-center rounded-full border border-white/20 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-white transition hover:border-white/40 hover:bg-white/10"
                        href="{trailer}"
                        target="_blank"
                        rel="noreferrer"
                      >
                        Watch trailer
                      </a>
                    </div>
                  </article>"""

horror1 = make_card("Get Out", "2017-02-24", "8.1", "Horror", "https://image.tmdb.org/t/p/w500/dzBootUD4I9T2nLdxyK17z0yFwE.jpg", "https://www.youtube.com/watch?v=DzfpyUB60YY")
horror2 = make_card("A Quiet Place", "2018-04-06", "8.1", "Horror", "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg", "https://www.youtube.com/watch?v=WR7cc5t7tv8")
horror_append = "\n" + horror1 + "\n" + horror2 + "\n"

thriller1 = make_card("Se7en", "1995-09-22", "8.6", "Thriller", "https://image.tmdb.org/t/p/w500/69SsnCRQRVKgGlOUQqX9HQgNV9g.jpg", "https://www.youtube.com/watch?v=znmZoVkCjpI")
thriller2 = make_card("Inception", "2010-07-16", "8.8", "Thriller", "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQIgTGvRv.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
thriller_append = "\n" + thriller1 + "\n" + thriller2 + "\n"

comedy1 = make_card("Superbad", "2007-08-17", "7.6", "Comedy", "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg", "https://www.youtube.com/watch?v=4eaZ_48ZYog")
comedy2 = make_card("Step Brothers", "2008-07-25", "7.0", "Comedy", "https://image.tmdb.org/t/p/w500/yA33Fw1alBTAz32Gf2hT167I4vT.jpg", "https://www.youtube.com/watch?v=CewglxElBK0")
comedy_append = "\n" + comedy1 + "\n" + comedy2 + "\n"

def insert_after(target_href, append_html, text):
    # We find target_href. Then we look for the next </article>
    pos = text.find(target_href)
    if pos == -1:
        print(f"Failed to find {target_href}")
        return text
    end_article = text.find("</article>", pos)
    if end_article == -1:
        return text
    end_article += len("</article>")
    
    return text[:end_article] + append_html + text[end_article:]

content = insert_after("href=\"https://www.youtube.com/watch?v=xU4bplQ2ZbY\"", horror_append, content)
content = insert_after("href=\"https://www.youtube.com/watch?v=AFuE1LRxm80\"", thriller_append, content)
content = insert_after("href=\"https://www.youtube.com/watch?v=5-7eWDBc40\"", comedy_append, content)

Path("static/index.html").write_text(content, encoding="utf-8")
print("Grids successfully patched!")
