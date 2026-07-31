const fs = require('fs');
const files = fs.readdirSync('dist/assets');
const cssFile = files.find(f => f.endsWith('.css'));
const css = fs.readFileSync('dist/assets/' + cssFile, 'utf8');

const regex = /\.bg-surface\b[^{]*\{[^}]*\}/g;
let match;
while ((match = regex.exec(css)) !== null) {
  console.log(match[0]);
}
