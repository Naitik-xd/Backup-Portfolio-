import re

with open('public/js/inline.js', 'r') as f:
    content = f.read()

# The first block starts with `document.addEventListener('DOMContentLoaded', () => {`
# and ends right before `function attachEvents() {`

start_idx = content.find("document.addEventListener('DOMContentLoaded', () => {")
end_idx = content.find("function attachEvents() {")

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    with open('public/js/inline.js', 'w') as f:
        f.write(content)
    print("Fixed duplicates")
else:
    print("Could not find blocks")
