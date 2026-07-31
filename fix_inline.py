import re

with open('index.html', 'r') as f:
    content = f.read()

# Find all inline scripts without src attribute
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)

with open('public/js/inline.js', 'w') as f:
    for script in scripts:
        f.write(script + '\n\n')

# Remove inline scripts
content = re.sub(r'<script>.*?</script>', '', content, flags=re.DOTALL)

# Replace CDN links with local links
content = re.sub(r'https://unpkg.com/lucide@[^/]+/dist/umd/lucide.min.js', '/js/lucide.min.js', content)
content = re.sub(r'https://cdnjs.cloudflare.com/ajax/libs/gsap/[^/]+/gsap.min.js', '/js/gsap.min.js', content)
content = re.sub(r'https://cdn.jsdelivr.net/npm/marked@[^/]+/marked.min.js', '/js/marked.min.js', content)

# Remove CDNs from CSP in index.html
content = re.sub(r' https://unpkg.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net', '', content)

with open('index.html', 'w') as f:
    f.write(content)

