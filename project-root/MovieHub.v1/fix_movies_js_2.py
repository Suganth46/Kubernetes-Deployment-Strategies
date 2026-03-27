import re
from pathlib import Path

content = Path("src/data/movies.js").read_text(encoding="utf-8")

horror_append = """      {
        id: 1198994,
        title: "Send Help",
        releaseDate: "2026-01-22",
        rating: 7.0,
        genre: "Horror Comedy",
        overview:
          "Two co-workers survive a crash and fight to escape a deadly island.",
        poster: `${posterBase}/mjkS2iAgWj3ik1DTjvI15nHZ7yl.jpg`,
        backdrop: `${backdropBase}/fBh0OlTY5XSHuFrQ7ylXHniwg9s.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=R4wiXj9NmEE",
      },
      {
        id: 1572073,
        title: "The Deadly Little Mermaid",
        releaseDate: "2026-03-06",
        rating: 5.4,
        genre: "Horror",
        overview:
          "A rescued stranger brings a curse ashore and turns a coastal home into a trap.",
        poster: `${posterBase}/uye25uG7k8r3NNPLyPiKOiRnFRF.jpg`,
        backdrop: `${backdropBase}/yzIjyPtwvyjHelxqIRXGpiaucPG.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=xU4bplQ2ZbY",
      },
      {
        id: 419430,
        title: "Get Out",
        releaseDate: "2017-02-24",
        rating: 8.1,
        genre: "Horror",
        overview: "A young African-American visits his white girlfriend's parents for the weekend.",
        poster: "https://images.unsplash.com/photo-1505634524240-41dbd2449553?auto=format&fit=crop&q=80&w=400",
        backdrop: "https://images.unsplash.com/photo-1505634524240-41dbd2449553?auto=format&fit=crop&q=80&w=400",
        trailerUrl: "https://www.youtube.com/watch?v=DzfpyUB60YY",
      },
      {
        id: 447332,
        title: "A Quiet Place",
        releaseDate: "2018-04-06",
        rating: 8.1,
        genre: "Horror",
        overview: "A family is forced to live in silence while hiding from creatures that hunt by sound.",
        poster: "https://images.unsplash.com/photo-1605806616949-1e87b487cb2a?auto=format&fit=crop&q=80&w=400",
        backdrop: "https://images.unsplash.com/photo-1605806616949-1e87b487cb2a?auto=format&fit=crop&q=80&w=400",
        trailerUrl: "https://www.youtube.com/watch?v=WR7cc5t7tv8",
      },"""

content = re.sub(r'      \{\n        id: 1198994,\n        title: "Send Help",.*?trailerUrl: "https://www.youtube.com/watch\?v=xU4bplQ2ZbY",\n      \},', horror_append, content, flags=re.DOTALL)


thriller_append = """      {
        id: 1290821,
        title: "Shelter",
        releaseDate: "2026-01-28",
        rating: 6.7,
        genre: "Action Thriller",
        overview:
          "A rescue on a remote island sparks a fight against enemies from the past.",
        poster: `${posterBase}/buPFnHZ3xQy6vZEHxbHgL1Pc6CR.jpg`,
        backdrop: `${backdropBase}/nHxWyy18SvAZ8jJeemtS8k1UNjM.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=PPMawzJxKF4",
      },
      {
        id: 1265609,
        title: "War Machine",
        releaseDate: "2026-02-12",
        rating: 7.3,
        genre: "Action Thriller",
        overview:
          "A combat engineer leads a unit through a mission against a massive killing machine.",
        poster: `${posterBase}/tlPgDzwIE7VYYIIAGCTUOnN4wI1.jpg`,
        backdrop: `${backdropBase}/6yeVcxFR0j08vlv2OlL6zbewm4D.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=AFuE1LRxm80",
      },
      {
        id: 807,
        title: "Se7en",
        releaseDate: "1995-09-22",
        rating: 8.6,
        genre: "Thriller",
        overview: "Two detectives, a rookie and a veteran, hunt a serial killer.",
        poster: "https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400",
        backdrop: "https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400",
        trailerUrl: "https://www.youtube.com/watch?v=znmZoVkCjpI",
      },
      {
        id: 27205,
        title: "Inception",
        releaseDate: "2010-07-16",
        rating: 8.8,
        genre: "Thriller",
        overview: "A thief who steals corporate secrets through the use of dream-sharing technology.",
        poster: "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?auto=format&fit=crop&q=80&w=400",
        backdrop: "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?auto=format&fit=crop&q=80&w=400",
        trailerUrl: "https://www.youtube.com/watch?v=YoHD9XEInc0",
      },"""

content = re.sub(r'      \{\n        id: 1290821,\n        title: "Shelter",.*?trailerUrl: "https://www.youtube.com/watch\?v=AFuE1LRxm80",\n      \},', thriller_append, content, flags=re.DOTALL)


comedy_append = """      {
        id: 1084242,
        title: "Zootopia 2",
        releaseDate: "2025-11-26",
        rating: 7.6,
        genre: "Animation Comedy",
        overview:
          "Judy and Nick go undercover again when a mystery throws the city off balance.",
        poster: `${posterBase}/oJ7g2CifqpStmoYQyaLQgEU32qO.jpg`,
        backdrop: `${backdropBase}/lgotj3xMoJZbynwHfcQcJAEMWH.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=BjkIOU5PhyQ",
      },
      {
        id: 1297842,
        title: "GOAT",
        releaseDate: "2026-02-11",
        rating: 7.6,
        genre: "Animation Comedy",
        overview:
          "A small goat gets a once-in-a-lifetime shot at a brutal pro sport.",
        poster: `${posterBase}/wfuqMlaExcoYiUEvKfVpUTt1v4u.jpg`,
        backdrop: `${backdropBase}/tq3h43fZy0H80vzf47MAY7R9Mxo.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=5-7eWDBc40",
      },
      {
        id: 8363,
        title: "Superbad",
        releaseDate: "2007-08-17",
        rating: 7.6,
        genre: "Comedy",
        overview: "Two co-dependent high school seniors are forced to deal with separation anxiety.",
        poster: "https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg",
        backdrop: "https://image.tmdb.org/t/p/w780/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg",
        trailerUrl: "https://www.youtube.com/watch?v=4eaZ_48ZYog",
      },
      {
        id: 13374,
        title: "Step Brothers",
        releaseDate: "2008-07-25",
        rating: 7.0,
        genre: "Comedy",
        overview: "Two aimless middle-aged losers still living at home are forced against their will to become roommates.",
        poster: "https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400",
        backdrop: "https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400",
        trailerUrl: "https://www.youtube.com/watch?v=CewglxElBK0",
      },"""

content = re.sub(r'      \{\n        id: 1084242,\n        title: "Zootopia 2",.*?trailerUrl: "https://www.youtube.com/watch\?v=5-7eWDBc40",\n      \},', comedy_append, content, flags=re.DOTALL)


Path("src/data/movies.js").write_text(content, encoding="utf-8")
print("Added missing items to movies.js")

