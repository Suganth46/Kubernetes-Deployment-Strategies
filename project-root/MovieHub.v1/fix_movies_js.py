import re
from pathlib import Path

content = Path("src/data/movies.js").read_text(encoding="utf-8")

replacements = {
    # The Notebook backdrop
    "https://image.tmdb.org/t/p/w780/qom1SZRENs404DnghMvD2hLzUo9.jpg": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&q=80&w=400",
    
    # Get Out (well, let's just make sure we replace the dzBoot string anywhere)
    "dzBootUD4I9T2nLdxyK17z0yFwE.jpg": "no-longer-used",
}

for old, new in replacements.items():
    content = content.replace(old, new)


# Add missing movies to movies.js just in case GenreShowcase is missing them!
# Wait, let's see what's in movies.js first.
Path("src/data/movies.js").write_text(content, encoding="utf-8")
print("Done movies.js")

