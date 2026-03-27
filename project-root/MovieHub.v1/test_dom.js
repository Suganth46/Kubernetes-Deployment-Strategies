const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const html = fs.readFileSync('static/index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('jsdomError', (err) => {
  fs.writeFileSync('error.log', err.stack || err.toString());
});

const dom = new JSDOM(html, { runScripts: 'dangerously', virtualConsole });
