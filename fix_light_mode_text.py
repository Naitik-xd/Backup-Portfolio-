import re

with open('index.html', 'r') as f:
    content = f.read()

target = """      body.light-mode .text-white\/75 {
        color: rgba(15, 23, 42, 0.75) !important;
      }"""

replacement = """      body.light-mode .text-white\/75 {
        color: rgba(15, 23, 42, 0.75) !important;
      }
      body.light-mode .text-white\/90 {
        color: rgba(15, 23, 42, 0.9) !important;
      }
      body.light-mode .text-white\/50 {
        color: rgba(15, 23, 42, 0.5) !important;
      }
      body.light-mode .text-white\/30 {
        color: rgba(15, 23, 42, 0.3) !important;
      }"""

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
