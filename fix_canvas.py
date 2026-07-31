with open('src/components/CanvasBackground.tsx', 'r') as f:
    content = f.read()

content = content.replace('<Environment files="/potsdamer_platz_1k.hdr" />', '<Environment preset="city" />')

with open('src/components/CanvasBackground.tsx', 'w') as f:
    f.write(content)
