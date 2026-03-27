import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

old_search = """            <div class="flex w-full flex-col gap-3 sm:flex-row md:w-auto">
              <input
                id="movie-search"
                type="search"
                placeholder="Search year, title, or genre"
                class="w-full rounded-full border border-white/15 bg-white/5 px-5 py-3 text-sm text-white placeholder:text-slate-400 focus:border-emerald-200/70 focus:outline-none"
              />
              <button"""
if old_search in content:
    print("Found old search")
else:
    print("Did NOT find old search")

old_script = """      const searchInput = document.getElementById("movie-search");
      const clearButton = document.getElementById("clear-filters");"""
if old_script in content:
    print("Found old script")
else:
    print("Did NOT find old script!")
