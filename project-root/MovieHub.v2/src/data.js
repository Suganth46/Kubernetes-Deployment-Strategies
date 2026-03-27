export const genres = ["All", "Action", "Sci-Fi", "Drama", "Crime", "Thriller", "Comedy"];
export const languages = ["All", "Telugu", "Tamil", "Hindi", "Malayalam", "English"];

export const movies = [
  // TELUGU
  {
    id: 1,
    title: "RRR",
    description: "A fictitious story about two legendary revolutionaries and their journey away from home.",
    rating: "8.8",
    genre: "Action",
    language: "Telugu",
    released: true,
    poster: "https://upload.wikimedia.org/wikipedia/en/d/d7/RRR_Poster.jpg",
    trailerLink: "https://www.youtube.com/watch?v=NgBoMJy386M",
    cast: ["N. T. Rama Rao Jr.", "Ram Charan", "Ajay Devgn", "Alia Bhatt"]
  },
  {
    id: 2,
    title: "Kalki 2898 AD",
    description: "A modern-day avatar of Vishnu, a Hindu god, who is believed to have descended to earth to protect the world.",
    rating: "7.6",
    genre: "Sci-Fi",
    language: "Telugu",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/rstcAnBeCkxNQjNp3YXrF6IP1tW.jpg",
    trailerLink: "https://www.youtube.com/watch?v=y1QhE7xH4-4",
    cast: ["Prabhas", "Amitabh Bachchan", "Kamal Haasan", "Deepika Padukone", "Disha Patani"]
  },
  {
    id: 3,
    title: "Pushpa: The Rise",
    description: "A story of a red sandalwood smuggler operating in the Seshachalam Hills of the Rayalaseema region of Andhra Pradesh.",
    rating: "7.6",
    genre: "Action",
    language: "Telugu",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/h6Pd89ngvl9quPVsx3KoJlQsvk9.jpg",
    trailerLink: "https://www.youtube.com/watch?v=pKctjlrbEkE",
    cast: ["Allu Arjun", "Fahadh Faasil", "Rashmika Mandanna", "Jagadeesh Prathap Bandari"]
  },

  // TAMIL
  {
    id: 4,
    title: "Leo",
    description: "Parthiban is a mild-mannered cafe owner in Kashmir, who fends off a gang of murderous thugs...",
    rating: "7.2",
    genre: "Action",
    language: "Tamil",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/gSOVog7ydsaF1YpgAqBqnKYFGY.jpg",
    trailerLink: "https://www.youtube.com/watch?v=Po3jStA673E",
    cast: ["Vijay", "Sanjay Dutt", "Arjun", "Trisha", "Gautham Vasudev Menon"]
  },
  {
    id: 5,
    title: "Vikram",
    description: "A special agent investigates a murder committed by a masked group of serial killers.",
    rating: "8.3",
    genre: "Action",
    language: "Tamil",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/d489L1rjwHdUQLt8kGLocj2zlyh.jpg",
    trailerLink: "https://www.youtube.com/watch?v=OKBMcl61N3o",
    cast: ["Kamal Haasan", "Vijay Sethupathi", "Fahadh Faasil", "Suriya"]
  },
  {
    id: 6,
    title: "Jailer",
    description: "A retired jailer goes on a manhunt to find his son's killers.",
    rating: "7.1",
    genre: "Action",
    language: "Tamil",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/64mHMdeZwwt2P6q1DFsP9wa4qX6.jpg",
    trailerLink: "https://www.youtube.com/watch?v=xenA_b1J7aY",
    cast: ["Rajinikanth", "Vinayakan", "Ramya Krishnan", "Vasanth Ravi", "Mohanlal"]
  },

  // HINDI
  {
    id: 7,
    title: "Jawan",
    description: "A high-octane action thriller which outlines the emotional journey of a man who is set to rectify the wrongs in the society.",
    rating: "7.0",
    genre: "Action",
    language: "Hindi",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/jFt1gS4BGHlK8xt76Y81Alp4dbt.jpg",
    trailerLink: "https://www.youtube.com/watch?v=COv52Qyctws",
    cast: ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi", "Deepika Padukone"]
  },
  {
    id: 8,
    title: "Pathaan",
    description: "An Indian spy takes on the leader of a group of mercenaries who have nefarious plans to target his homeland.",
    rating: "5.9",
    genre: "Action",
    language: "Hindi",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/arf00BkwvXo0CFKbaD9OpqdE4Nu.jpg",
    trailerLink: "https://www.youtube.com/watch?v=vqu4z34wENw",
    cast: ["Shah Rukh Khan", "Deepika Padukone", "John Abraham", "Dimple Kapadia"]
  },
  {
    id: 9,
    title: "Animal",
    description: "A son undergoes a remarkable transformation as the bond with his father begins to fracture.",
    rating: "6.2",
    genre: "Crime",
    language: "Hindi",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/hr9rjR3J0xBBKmlJ4n3gHId9ccx.jpg",
    trailerLink: "https://www.youtube.com/watch?v=8FkLRcU4p0A",
    cast: ["Ranbir Kapoor", "Anil Kapoor", "Bobby Deol", "Rashmika Mandanna"]
  },

  // MALAYALAM
  {
    id: 10,
    title: "Manjummel Boys",
    description: "A group of friends gets into a daring rescue mission to save their friend from Guna Caves, a perilously deep pit.",
    rating: "8.3",
    genre: "Thriller",
    language: "Malayalam",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/bswrtewwthpsh6nABiqKevU4UBI.jpg",
    trailerLink: "https://www.youtube.com/watch?v=id848Ww1YLo",
    cast: ["Soubin Shahir", "Sreenath Bhasi", "Balu Varghese", "Ganapathi"]
  },
  {
    id: 11,
    title: "Premalu",
    description: "Sachin pursues romance but finds himself caught between two potential partners.",
    rating: "7.9",
    genre: "Comedy",
    language: "Malayalam",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/uPpmBjY3znUqGY8kYwI5xvOrSc0.jpg",
    trailerLink: "https://www.youtube.com/watch?v=f_V0mIKtDE8",
    cast: ["Naslen K. Gafoor", "Mamitha Baiju", "Shyam Mohan", "Sangeeth Prathap"]
  },

  // ENGLISH
  {
    id: 12,
    title: "Oppenheimer",
    description: "The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic bomb.",
    rating: "8.4",
    genre: "Drama",
    language: "English",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
    trailerLink: "https://www.youtube.com/watch?v=uYPbbksJxIg",
    cast: ["Cillian Murphy", "Emily Blunt", "Matt Damon", "Robert Downey Jr."]
  },
  {
    id: 13,
    title: "Dune: Part Two",
    description: "Paul Atreides unites with Chani and the Fremen while acting as their leader.",
    rating: "8.6",
    genre: "Sci-Fi",
    language: "English",
    released: true,
    poster: "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg",
    trailerLink: "https://www.youtube.com/watch?v=Way9Dexny3w",
    cast: ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson", "Javier Bardem"]
  }
];

export const newReleases = movies.slice(0, 3);
