const fs = require('fs');

let movies = fs.readFileSync('src/data/movies.js', 'utf8');

// I'll be smart and just replace finding the exact strings from temp.js
const r1 = \	railerUrl: "https://www.youtube.com/watch?v=3fLCdIYShEQ",
        },
        {
          id: 313369,
          title: "La La Land",
          releaseDate: "2016-12-29",
          rating: 8.0,
          genre: "Romance Musical",
          overview: "Mia and Sebastian are struggling to make ends meet in a city known for crushing hopes.",
          poster: \\\\/uDO8zWDhfWwoFdKS4fblf7PckaK.jpg\\\,
          backdrop: \\\\/qJeU7KM4nT2C1WpOrwPcSDGFUWE.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=0pdqf4P9MB8",
        },
        {
          id: 11036,
          title: "The Notebook",
          releaseDate: "2004-06-25",
          rating: 7.9,
          genre: "Romance Drama",
          overview: "An epic love story centered around an older man who reads aloud to a woman.",
          poster: \\\\/rNzQyW4f8B8cQeg7Dgj3n6eT5k9.jpg\\\,
          backdrop: \\\\/qom1SZRENs404DnghMvD2hLzUo9.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=FC6biTjEyZw",
        },\;
movies = movies.replace(/trailerUrl:\s*"https:\/\/www\.youtube\.com\/watch\?v=3fLCdIYShEQ",\s*\},/, r1);

const r2 = \	railerUrl: "https://www.youtube.com/watch?v=1ZWe3i3xS0Y",
        },
        {
          id: 419430,
          title: "Get Out",
          releaseDate: "2017-02-24",
          rating: 7.6,
          genre: "Horror",
          overview: "Chris uncovers a disturbing secret at his girlfriend's parents' estate.",
          poster: \\\\/tFXcEccSQAmRoIdcgGOSNpe2AON.jpg\\\,
          backdrop: \\\\/7bSQ2WihNIVaZ0E7Btv440rN8rV.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=DzfpyUB60YY",
        },
        {
          id: 447332,
          title: "A Quiet Place",
          releaseDate: "2018-04-06",
          rating: 7.5,
          genre: "Horror",
          overview: "A family is forced to live in silence while hiding from creatures.",
          poster: \\\\/nAU74GmpUk7t5iklEp3bufwDq4n.jpg\\\,
          backdrop: \\\\/roYyPiQmuvnLSFw1I3k9sFq1K12.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=WR7cc5t7tv8",
        },\;
movies = movies.replace(/trailerUrl:\s*"https:\/\/www\.youtube\.com\/watch\?v=1ZWe3i3xS0Y",\s*\},/, r2);

const r3 = \	railerUrl: "https://www.youtube.com/watch?v=_QeL9N733yA",
        },
        {
          id: 807,
          title: "Se7en",
          releaseDate: "1995-09-22",
          rating: 8.6,
          genre: "Thriller",
          overview: "Two detectives hunt a serial killer.",
          poster: \\\\/6yoghtyTpznpBik8EngEmJskVPh.jpg\\\,
          backdrop: \\\\/2yFqQ8IivvI1t4lO1fXyAmlZzEY.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=znmZoVkCjpI",
        },
        {
          id: 27205,
          title: "Inception",
          releaseDate: "2010-07-16",
          rating: 8.8,
          genre: "Thriller",
          overview: "A thief is given the inverse task of planting an idea.",
          poster: \\\\/9gk7adHYeDvHkYSBAtJTrA4Xz9r.jpg\\\,
          backdrop: \\\\/ztZ4vw151mw04Bg6rqJLQGAA40Z.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=YoHD9XEInc0",
        },\;
movies = movies.replace(/trailerUrl:\s*"https:\/\/www\.youtube\.com\/watch\?v=_QeL9N733yA",\s*\},/, r3);

const r4 = \	railerUrl: "https://www.youtube.com/watch?v=1v_H1lK-3jE",
        },
        {
          id: 8363,
          title: "Superbad",
          releaseDate: "2007-08-17",
          rating: 7.3,
          genre: "Comedy",
          overview: "Two co-dependent high school seniors plan to stage a booze-soaked party.",
          poster: \\\\/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg\\\,
          backdrop: \\\\/dO3HjXv40129gM6e7r7vV2f6FvI.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=MN8fVMcHLew",
        },
        {
          id: 12133,
          title: "Step Brothers",
          releaseDate: "2008-07-25",
          rating: 7.1,
          genre: "Comedy",
          overview: "Two aimless middle-aged losers are forced to become room-mates.",
          poster: \\\\/jVpAFWLSgXbM085j0n6837HkE7q.jpg\\\,
          backdrop: \\\\/2qH6w7Kk7t6K3YhM7JXVm08gHkG.jpg\\\,
          trailerUrl: "https://www.youtube.com/watch?v=CewglxElBK0",
        },\;
movies = movies.replace(/trailerUrl:\s*"https:\/\/www\.youtube\.com\/watch\?v=1v_H1lK-3jE",\s*\},/, r4);

fs.writeFileSync('src/data/movies.js', movies, 'utf8');
console.log('done replacing');
