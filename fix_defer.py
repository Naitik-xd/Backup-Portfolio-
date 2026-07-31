import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('<script src="https://unpkg.com/lucide@latest"></script>', '<script defer src="https://unpkg.com/lucide@latest"></script>')
content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>', '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>')
content = content.replace('<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>', '<script defer src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>')

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
