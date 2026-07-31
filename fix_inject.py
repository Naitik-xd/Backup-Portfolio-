with open('index.html', 'r') as f:
    content = f.read()

if '<script defer src="/js/inline.js"></script>' not in content:
    content = content.replace('</body>', '    <script defer src="/js/inline.js"></script>\n  </body>')

with open('index.html', 'w') as f:
    f.write(content)
