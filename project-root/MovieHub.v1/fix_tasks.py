import re
import os

html_path = "static/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove search bar
search_html_pattern = r'<section class="flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/5 px-6 py-5 backdrop-blur md:flex-row md:items-center md:justify-between">.*?</section>'
content = re.sub(search_html_pattern, '', content, flags=re.DOTALL)

# 2. Remove search JS
js_remove_pattern = r'const searchInput = document.getElementById\("movie-search"\);[\s\S]*?applyFilters\(\);\n    \}\);\n\n    applyFilters\(\);'
content = re.sub(js_remove_pattern, '', content)

# 3. Replace broken images
replacements = {
    'https://images.unsplash.com/photo-1505634524240-41dbd2449553?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/tXxtAWX4Xogk1P1aC2vMOrL0uV7.jpg', # get out
    'https://images.unsplash.com/photo-1605806616949-1e87b487cb2a?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg', # quiet place
    'https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVPh.jpg', # se7en
    'https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg', # inception
    'https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/gfVQvO2Qz9n352rBsh0D4ZqL0Uo.jpg', # step brothers
}
for old_str, new_str in replacements.items():
    content = content.replace(old_str, new_str)

# 4. Update the form to mailto
old_form = '<form class="flex w-full max-w-md flex-col gap-3 sm:flex-row">'
new_form = '<form action="mailto:selvamthiru712@gmail.com" method="post" enctype="text/plain" class="flex w-full max-w-md flex-col gap-3 sm:flex-row">'
content = content.replace(old_form, new_form)

# 5. Add Login link to header
old_nav = """          <nav class="flex flex-wrap gap-4 text-xs uppercase tracking-[0.2em] text-slate-300">
            <a class="transition hover:text-white" href="#">Reviews</a>
            <a class="transition hover:text-white" href="#">Watchlists</a>
            <a class="transition hover:text-white" href="#">Editorial</a>
          </nav>"""
new_nav = """          <nav class="flex flex-wrap gap-4 text-xs uppercase tracking-[0.2em] text-slate-300">
            <a class="transition hover:text-white" href="#">Reviews</a>
            <a class="transition hover:text-white" href="#">Watchlists</a>
            <a class="transition hover:text-white" href="#">Editorial</a>
            <a class="transition hover:text-white text-emerald-200" href="login.html">Login</a>
          </nav>"""
content = content.replace(old_nav, new_nav)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated static/index.html")
