with open('index.html', 'r') as f:
    content = f.read()

camera_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="animate-pulse"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>'''

content = content.replace('<i data-lucide="camera" class="w-10 h-10 text-white animate-pulse"></i>', camera_svg)

with open('index.html', 'w') as f:
    f.write(content)
