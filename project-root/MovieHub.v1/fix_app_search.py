import re
from pathlib import Path

content = Path("src/App.jsx").read_text(encoding="utf-8")

old_search = """              <div className="flex w-full flex-col gap-3 sm:flex-row md:w-auto">
                <input
                  type="search"
                  value={search}
                  onChange={(event) => setSearch(event.target.value)}
                  placeholder="Search year, title, or genre"
                  className="w-full rounded-full border border-white/15 bg-white/5 px-5 py-3 text-sm text-white placeholder:text-slate-400 focus:border-emerald-200/70 focus:outline-none"
                />
                <button"""

new_search = """              <div className="flex w-full flex-col gap-3 sm:flex-row md:w-auto">
                <div className="relative w-full sm:w-80">
                  <svg className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-400 cursor-pointer transition hover:text-emerald-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <path d="m21 21-4.3-4.3"></path>
                  </svg>
                  <input
                    type="search"
                    value={search}
                    onChange={(event) => setSearch(event.target.value)}
                    placeholder="Search year, title, or genre"
                    className="w-full rounded-full border border-white/15 bg-white/5 pl-12 pr-5 py-3 text-sm text-white placeholder:text-slate-400 focus:border-emerald-200/70 focus:outline-none"
                  />
                </div>
                <button"""

content = content.replace(old_search, new_search)
Path("src/App.jsx").write_text(content, encoding="utf-8")
print("App Fixed")
