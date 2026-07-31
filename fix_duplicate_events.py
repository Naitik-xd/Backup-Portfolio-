import re

with open('public/js/inline.js', 'r') as f:
    content = f.read()

# We want to remove this block:
block_start = "document.addEventListener('DOMContentLoaded', () => {"
block_end = "function attachEvents() {"

start_idx = content.find(block_start)
# We only want to remove up to just before function attachEvents()
end_idx = content.find(block_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    with open('public/js/inline.js', 'w') as f:
        f.write(content)
    print("Fixed duplicate events successfully.")
else:
    print("Block not found!")
