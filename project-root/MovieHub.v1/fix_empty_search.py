import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

# Fix broken image URLs
replacements = {
    # The Notebook backdrop
    "https://image.tmdb.org/t/p/w780/qom1SZRENs404DnghMvD2hLzUo9.jpg": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&q=80&w=400",
    
    # Get Out
    "https://image.tmdb.org/t/p/w500/dzBootUD4I9T2nLdxyK17z0yFwE.jpg": "https://images.unsplash.com/photo-1505634524240-41dbd2449553?auto=format&fit=crop&q=80&w=400",
    
    # A Quiet Place
    "https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg": "https://images.unsplash.com/photo-1605806616949-1e87b487cb2a?auto=format&fit=crop&q=80&w=400",
    
    # Se7en
    "https://image.tmdb.org/t/p/w500/69SsnCRQRVKgGlOUQqX9HQgNV9g.jpg": "https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400",
    
    # Inception
    "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQIgTGvRv.jpg": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?auto=format&fit=crop&q=80&w=400",
    
    # Step Brothers
    "https://image.tmdb.org/t/p/w500/yA33Fw1alBTAz32Gf2hT167I4vT.jpg": "https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400",
}

for old, new in replacements.items():
    content = content.replace(old, new)


# Update the article class to be searchable
# Original missing dataset
def add_search_data(match):
    full_str = match.group(0)
    # Extract the title from the h4 or h3
    title_match = re.search(r'<h[34][^>]*>(.*?)</h[34]>', full_str)
    title = title_match.group(1).strip() if title_match else "unknown"
    
    # Check if it already has data-title
    if 'data-title=' not in full_str:
        # replace the starting article tag
        # wait! I need to know category. We can just add `.searchable-card` to the class, and `data-title="{title.lower()}"`
        new_tag = f'<article class="searchable-card group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40" data-title="{title.lower()}"'
        str_out = re.sub(r'<article class="group flex h-full flex-col overflow-hidden rounded-2xl border border-white/10 bg-slate-950/60 transition hover:-translate-y-1 hover:border-emerald-200/40"', new_tag, full_str, count=1)
        return str_out
    return full_str

# Apply to all articles within grids that are missing data-title
# Wait, let's just make ALL `.imdb-card` use `.searchable-card` too, or adjust applyFilters to target `.searchable-card`
# Or better, just inject `data-title="..."` into all `<article>` tags in the document that lack it
articles = re.split(r'(<article\b.*?</article>)', content, flags=re.DOTALL)
new_articles = []
for p in articles:
    if p.startswith('<article'):
        if 'data-title=' not in p:
            title_m = re.search(r'<h[34][^>]*>(.*?)</h[34]>', p)
            if title_m:
                t = title_m.group(1).strip().lower()
                p = re.sub(r'<article\s+class="([^"]+)"', r'<article class="\1 searchable-card" data-title="' + t + '"', p, count=1)
        else:
            p = re.sub(r'<article\s+class="([^"]+)"', r'<article class="\1 searchable-card"', p, count=1)
    new_articles.append(p)

content = "".join(new_articles)

# Finally, update applyFilters to query `.searchable-card` instead of `.imdb-card[data-year]`
content = content.replace(
    'document.querySelectorAll(".imdb-card[data-year]")',
    'document.querySelectorAll(".searchable-card")'
)

# And in applyFilters, year might be missing. So fallback to ""
content = content.replace(
    'const year = card.dataset.year;',
    'const year = card.dataset.year || "";'
)

# Also fix the JS where it toggles hidden on noResults - actually wait, wait, the `grid` parent might be left empty. Let's just do standard filter.
Path("static/index.html").write_text(content, encoding="utf-8")
print("Done index.html")
