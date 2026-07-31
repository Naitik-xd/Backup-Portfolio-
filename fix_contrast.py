with open('index.html', 'r') as f:
    content = f.read()

# Change --text-dim in dark mode
content = content.replace('--text-dim: #94a3b8;', '--text-dim: #b4becd;')
# Change --text-dim in light mode
content = content.replace('--text-dim: #475569;', '--text-dim: #334155;')

with open('index.html', 'w') as f:
    f.write(content)
