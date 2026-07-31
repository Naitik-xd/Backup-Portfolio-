with open('index.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if '// Global Skill details mapping object' in line:
        new_lines.append('    <script>\n')
    if '<!-- ── CHAT WIDGET ── -->' in line:
        new_lines.append('    </script>\n')
    if 'let chatHistory = [];' in line:
        new_lines.append('    <script>\n')
    if '<script type="module" src="/src/main.tsx"></script>' in line:
        new_lines.append('    </script>\n')
    
    new_lines.append(line)

with open('index.html', 'w') as f:
    f.writelines(new_lines)
