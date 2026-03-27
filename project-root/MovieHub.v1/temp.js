const posterBase = "https://image.tmdb.org/t/p/w500";
const backdropBase = "https://image.tmdb.org/t/p/w780";

export const nowPlaying = [
  {
    id: 687163,
    title: "Project Hail Mary",
    releaseDate: "2026-03-15",
    rating: 8.2,
    genre: "Sci-Fi Adventure",
    overview:
      "A teacher-turned-astronaut wakes up light years from home and must save Earth from a dying sun.",
    poster: `${posterBase}/yihdXomYb5kTeSivtFndMy5iDmf.jpg`,
    backdrop: `${backdropBase}/8Tfys3mDZVp4tNoH2ktm06a0Tau.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=m08TxIsFTRI",
  },
  {
    id: 875828,
    title: "Peaky Blinders: The Immortal Man",
    releaseDate: "2026-03-05",
    rating: 7.4,
    genre: "Crime Drama",
    overview:
      "Tommy Shelby returns to Birmingham to stop a plot that threatens his family and his country.",
    poster: `${posterBase}/gRMalasZEzsZi4w2VFuYusfSfqf.jpg`,
    backdrop: `${backdropBase}/1fkuBPid72KGS6WmtkEXMftZtkE.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=lcvUGs3xaDM",
  },
  {
    id: 1171145,
    title: "Crime 101",
    releaseDate: "2026-02-11",
    rating: 7.0,
    genre: "Crime Thriller",
    overview:
      "A relentless detective closes in on a thief running high-stakes heists along the 101 freeway.",
    poster: `${posterBase}/heMdO64ys1hR896YE2jvTv8JlBX.jpg`,
    backdrop: `${backdropBase}/52AkwEfQiJl2HuTPMZ2yC5Bdr9I.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=f5y-cziwmMw",
  },
  {
    id: 1159559,
    title: "Scream 7",
    releaseDate: "2026-02-25",
    rating: 5.8,
    genre: "Horror Mystery",
    overview:
      "A new Ghostface stalks a quiet town, forcing Sidney to confront her darkest fears.",
    poster: `${posterBase}/jjyuk0edLiW8vOSnlfwWCCLpbh5.jpg`,
    backdrop: `${backdropBase}/hz7TdCrpLLt2Dz7S3PS2HG9rpAO.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=4g8OciWNJn4",
  },
  {
    id: 1290821,
    title: "Shelter",
    releaseDate: "2026-01-28",
    rating: 6.7,
    genre: "Action Thriller",
    overview:
      "A self-exiled man rescues a girl from a storm and draws enemies from his past.",
    poster: `${posterBase}/buPFnHZ3xQy6vZEHxbHgL1Pc6CR.jpg`,
    backdrop: `${backdropBase}/nHxWyy18SvAZ8jJeemtS8k1UNjM.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=PPMawzJxKF4",
  },
];

export const genreSections = [
  {
    key: "romance",
    title: "Romance",
    description: "Stories for the hopelessly devoted.",
    movies: [
      {
        id: 597,
        title: "Titanic",
        releaseDate: "1997-12-18",
        rating: 7.9,
        genre: "Romance Drama",
        overview:
          "Two lovers aboard a doomed voyage fight for each other and their future.",
        poster: `${posterBase}/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg`,
        backdrop: `${backdropBase}/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=oHY7D7K58BM",
      },
      {
        id: 1316092,
        title: "Wuthering Heights",
        releaseDate: "2026-02-11",
        rating: 6.4,
        genre: "Romance Drama",
        overview:
          "A tragic love story ignites across the Yorkshire moors and refuses to die.",
        poster: `${posterBase}/3YBce6dTh1D5oCMITXk2S5QhPt.jpg`,
        backdrop: `${backdropBase}/vSQSYd2zZTqc0zmHImwWEGGluMI.jpg`,
        trailerUrl: "https://www.youtube.com/watch?v=3fLCdIYShEQ",
      },
    ],
  },
  {
    key: "horror",
    title: "Horror",
    description: "Keep the lights on tonight.",
    movies: [
      {
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
    ],
  },
  {
    key: "thriller",
    title: "Thriller",
    description: "High stakes and higher tension.",
    movies: [
      {
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
    ],
  },
  {
    key: "comedy",
    title: "Comedy",
    description: "Bright, loud, and impossible to ignore.",
    movies: [
      {
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
    ],
  },
];

export const imdbTop = [
  {
    id: 278,
    title: "The Shawshank Redemption",
    releaseDate: "1994-09-23",
    rating: 8.7,
    genre: "Drama",
    overview:
      "Two imprisoned men bond over years, finding solace and redemption through acts of decency.",
    poster: `${posterBase}/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg`,
    backdrop: `${backdropBase}/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=PLl99DlL6b0",
  },
  {
    id: 238,
    title: "The Godfather",
    releaseDate: "1972-03-14",
    rating: 8.7,
    genre: "Crime Drama",
    overview:
      "The aging patriarch of a crime dynasty transfers control to his reluctant son.",
    poster: `${posterBase}/3bhkrj58Vtu7enYsRolD1fZdja1.jpg`,
    backdrop: `${backdropBase}/tSPT36ZKlP2WVHJLM4cQPLSzv3b.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=8V2k2YQEQJ4",
  },
  {
    id: 424,
    title: "Schindler's List",
    releaseDate: "1993-12-15",
    rating: 8.6,
    genre: "History Drama",
    overview:
      "An industrialist saves more than a thousand lives during World War II.",
    poster: `${posterBase}/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg`,
    backdrop: `${backdropBase}/zb6fM1CX41D9rF9hdgclu0peUmy.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=v0RB-3sWbBA",
  },
  {
    id: 155,
    title: "The Dark Knight",
    releaseDate: "2008-07-16",
    rating: 8.5,
    genre: "Action Crime",
    overview:
      "Batman battles the Joker as Gotham descends into chaos.",
    poster: `${posterBase}/qJ2tW6WMUDux911r6m7haRef0WH.jpg`,
    backdrop: `${backdropBase}/dqK9Hag1054tghRQSqLSfrkvQnA.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=EXeTwQWrcwY",
  },
  {
    id: 597,
    title: "Titanic",
    releaseDate: "1997-12-18",
    rating: 7.9,
    genre: "Romance Drama",
    overview:
      "Two lovers aboard a doomed voyage fight for each other and their future.",
    poster: `${posterBase}/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg`,
    backdrop: `${backdropBase}/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg`,
    trailerUrl: "https://www.youtube.com/watch?v=oHY7D7K58BM",
  },
  {
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
];
