import re

with open('index.html', 'r') as f:
    content = f.read()

target = """      body.light-mode .text-white\/30 {
        color: rgba(15, 23, 42, 0.3) !important;
      }"""

replacement = """      body.light-mode .text-white\/30 {
        color: rgba(15, 23, 42, 0.3) !important;
      }
      body.light-mode .text-white\/70 {
        color: rgba(15, 23, 42, 0.7) !important;
      }
      body.light-mode .text-white\/80 {
        color: rgba(15, 23, 42, 0.8) !important;
      }
      body.light-mode .group-hover\:text-white\/80:hover {
        color: rgba(15, 23, 42, 0.8) !important;
      }"""

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
