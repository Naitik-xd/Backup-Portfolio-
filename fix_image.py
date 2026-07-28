import re

with open('index.html', 'r') as f:
    content = f.read()

target = "https://i.ibb.co/yFfgzbsP/sky-tower-1.jpg"
replacement = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&q=80&w=1000"

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
