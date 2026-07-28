import re

with open('index.html', 'r') as f:
    content = f.read()

target = """      .marquee-divider {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        background-color: #07091a;
        border-top: 1px solid rgba(255,255,255,0.03);
        border-bottom: 1px solid rgba(255,255,255,0.03);
        padding: 0.85rem 0;
        opacity: 0.12;
        user-select: none;
        pointer-events: none;
      }"""

replacement = """      .marquee-divider {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        background-color: #07091a;
        border-top: 1px solid rgba(255,255,255,0.03);
        border-bottom: 1px solid rgba(255,255,255,0.03);
        padding: 0.85rem 0;
        opacity: 0.4;
        user-select: none;
        pointer-events: none;
      }"""

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
