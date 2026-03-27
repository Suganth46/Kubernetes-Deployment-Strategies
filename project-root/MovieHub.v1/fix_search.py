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

new_search = """            <div class="flex w-full flex-col gap-3 sm:flex-row md:w-auto">
              <div class="relative w-full sm:w-80">
                <svg id="search-icon" class="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-400 cursor-pointer transition hover:text-emerald-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="11" cy="11" r="8"></circle>
                  <path d="m21 21-4.3-4.3"></path>
                </svg>
                <input
                  id="movie-search"
                  type="search"
                  placeholder="Search year, title, or genre"
                  class="w-full rounded-full border border-white/15 bg-white/5 pl-12 pr-5 py-3 text-sm text-white placeholder:text-slate-400 focus:border-emerald-200/70 focus:outline-none"
                />
              </div>
              <button"""

content = content.replace(old_search, new_search)

# And add the click listener for the search icon!
old_script = """      const searchInput = document.getElementById("movie-search");
      const clearButton = document.getElementById("clear-filters");"""

new_script = """      const searchInput = document.getElementById("movie-search");
      const searchIcon = document.getElementById("search-icon");
      const clearButton = document.getElementById("clear-filters");
      
      if (searchIcon) {
        searchIcon.addEventListener("click", () => searchInput.focus());
      }"""

content = content.replace(old_script, new_script)

Path("static/index.html").write_text(content, encoding="utf-8")
print("Search fixed")
