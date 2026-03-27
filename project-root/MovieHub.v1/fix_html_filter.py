import re
from pathlib import Path

content = Path("static/index.html").read_text(encoding="utf-8")

old_filter = """    const applyFilters = () => {
      const searchText = searchInput.value.trim().toLowerCase();
      let visibleCount = 0;

      cards.forEach((card) => {
        const year = card.dataset.year || "";
        const title = card.dataset.title || "";
        const genre = card.dataset.genre || "";

        const matchesGenre = !activeGenre || genre.includes(activeGenre);
        const matchesSearch =
          !searchText ||
          title.includes(searchText) ||
          genre.includes(searchText) ||
          year.includes(searchText);

        const isVisible = matchesSearch && matchesGenre;

        card.classList.toggle("hidden", !isVisible);
        if (isVisible) {
          visibleCount += 1;
        }
      });

      noResults.classList.toggle("hidden", visibleCount > 0);
    };"""

new_filter = """    const applyFilters = () => {
      const searchText = searchInput.value.trim().toLowerCase();
      let visibleCount = 0;

      cards.forEach((card) => {
        const year = card.dataset.year || "";
        const title = card.dataset.title || "";
        const genre = card.dataset.genre || "";

        const matchesGenre = !activeGenre || genre.includes(activeGenre);
        const matchesSearch =
          !searchText ||
          title.includes(searchText) ||
          genre.includes(searchText) ||
          year.includes(searchText);

        const isVisible = matchesSearch && matchesGenre;

        card.classList.toggle("hidden", !isVisible);
        if (isVisible) {
          visibleCount += 1;
        }
      });

      // Also hide empty genre sections
      document.querySelectorAll('.space-y-4').forEach(section => {
        // Find if this is a genre section (has a grid of cards)
        const grid = section.querySelector('.grid');
        if (grid) {
          const visibleCards = grid.querySelectorAll('.searchable-card:not(.hidden)');
          section.classList.toggle('hidden', visibleCards.length === 0);
        }
      });

      noResults.classList.toggle("hidden", visibleCount > 0);
    };"""

content = content.replace(old_filter, new_filter)

Path("static/index.html").write_text(content, encoding="utf-8")
print("Done styling index.html filters")
