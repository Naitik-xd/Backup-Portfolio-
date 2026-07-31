import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the camera icon wrapper with flex items-center justify-center
content = content.replace(
    'class="bg-surface/80 border border-outline p-5 rounded-full shadow-[0_0_30px_rgba(245,166,35,0.35)] transform scale-75 group-hover:scale-100 transition-transform duration-500"',
    'class="bg-surface/80 border border-outline w-24 h-24 rounded-full shadow-[0_0_30px_rgba(245,166,35,0.35)] transform scale-75 group-hover:scale-100 transition-transform duration-500 flex items-center justify-center"'
)

# Also make the opacity visible on mobile since hover doesn't work well
# Change `opacity-0 group-hover:opacity-100` to `opacity-100 md:opacity-0 group-hover:opacity-100`
content = content.replace(
    'class="absolute inset-0 bg-transparent/40 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-center justify-center z-20 pointer-events-none"',
    'class="absolute inset-0 bg-transparent/40 backdrop-blur-[2px] opacity-100 md:opacity-0 md:group-hover:opacity-100 transition-opacity duration-500 flex items-center justify-center z-20 pointer-events-none"'
)

with open('index.html', 'w') as f:
    f.write(content)
