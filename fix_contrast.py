import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix --text-dim color from #6b7494 to #94a3b8
content = content.replace('--text-dim: #6b7494;', '--text-dim: #94a3b8;')

# Fix light mode --text-dim from #64748b to #475569
content = content.replace('--text-dim: #64748b;', '--text-dim: #475569;')

# Fix marquee opacity in dark mode
content = content.replace('opacity: 0.4;\n        user-select: none;', 'opacity: 0.7;\n        user-select: none;')

# Fix marquee opacity in light mode
content = content.replace('body.light-mode .marquee-divider {\n        background-color: var(--background) !important;\n        border-top: 1px solid var(--outline) !important;\n        border-bottom: 1px solid var(--outline) !important;\n        opacity: 0.35;\n      }', 'body.light-mode .marquee-divider {\n        background-color: var(--background) !important;\n        border-top: 1px solid var(--outline) !important;\n        border-bottom: 1px solid var(--outline) !important;\n        opacity: 0.7;\n      }')

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
