with open('index.html', 'r') as f:
    content = f.read()

if 'name="robots" content="noindex' not in content:
    content = content.replace('</title>', '</title>\n    <meta name="robots" content="noindex, nofollow" />')
    with open('index.html', 'w') as f:
        f.write(content)
    print("Added noindex tag")
else:
    print("Already has noindex tag")
