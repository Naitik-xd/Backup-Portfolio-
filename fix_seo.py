with open('index.html', 'r') as f:
    content = f.read()

# Add meta description
content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0" />', '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\\n    <meta name="description" content="Naitik Agarwal\'s AI-Native Portfolio. I am a full-stack developer focusing on AI integration and modern web applications." />')

# Remove robots noindex
content = content.replace('<meta name="robots" content="noindex, nofollow" />', '')

with open('index.html', 'w') as f:
    f.write(content)
