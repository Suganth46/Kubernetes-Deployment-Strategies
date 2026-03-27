import re

app_path = "src/App.jsx"
with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the search bar section
search_section_regex = r'<section className="flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/5 px-6 py-5 backdrop-blur md:flex-row md:items-center md:justify-between">.*?</section>'
content = re.sub(search_section_regex, '', content, flags=re.DOTALL)

# Add login link
old_nav = """          <nav className="flex flex-wrap gap-4 text-xs uppercase tracking-[0.2em] text-slate-300">
            <a className="transition hover:text-white" href="#">Reviews</a>
            <a className="transition hover:text-white" href="#">Watchlists</a>
            <a className="transition hover:text-white" href="#">Editorial</a>
          </nav>"""
new_nav = """          <nav className="flex flex-wrap gap-4 text-xs uppercase tracking-[0.2em] text-slate-300">
            <a className="transition hover:text-white" href="#">Reviews</a>
            <a className="transition hover:text-white" href="#">Watchlists</a>
            <a className="transition hover:text-white" href="#">Editorial</a>
            <a className="transition hover:text-white text-emerald-200" href="/static/login.html">Login</a>
          </nav>"""
content = content.replace(old_nav, new_nav)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated App.jsx")
