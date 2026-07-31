with open('index.html', 'r') as f:
    content = f.read()

# Add bg-surface override for light mode
css_to_insert = """
      body.light-mode .bg-surface {
        background-color: var(--surface) !important;
      }
"""
if "body.light-mode .bg-surface {" not in content:
    content = content.replace("body.light-mode .bg-surface\\/30 {", css_to_insert + "      body.light-mode .bg-surface\\/30 {")

# Fix photography text colors
content = content.replace(
    '<h3 class="font-sora font-bold text-white text-2xl md:text-4xl">Sky Tower</h3>',
    '<h3 class="font-sora font-bold text-[#ffffff] text-2xl md:text-4xl">Sky Tower</h3>'
)
content = content.replace(
    '<span class="text-textDim font-space text-[10px] md:text-xs tracking-wider uppercase font-semibold">MDI GURUGRAM',
    '<span class="text-[#ffffff]/70 font-space text-[10px] md:text-xs tracking-wider uppercase font-semibold">MDI GURUGRAM'
)
content = content.replace(
    '<span class="font-space text-[9px] uppercase tracking-wider text-textDim mt-0.5">COMPETITION RANKING</span>',
    '<span class="font-space text-[9px] uppercase tracking-wider text-[#ffffff]/70 mt-0.5">COMPETITION RANKING</span>'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Patched!")
