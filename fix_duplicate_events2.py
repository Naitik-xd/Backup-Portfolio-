with open('public/js/inline.js', 'r') as f:
    content = f.read()

# find the second occurrence
block_start = "document.addEventListener('DOMContentLoaded', () => {"
first_idx = content.find(block_start)
second_idx = content.find(block_start, first_idx + 1)

block_end = "function attachEvents() {"
end_idx = content.find(block_end)

if second_idx != -1 and end_idx != -1:
    # Delete from second_idx to end_idx
    content = content[:second_idx] + content[end_idx:]
    with open('public/js/inline.js', 'w') as f:
        f.write(content)
    print("Fixed duplicate events correctly.")
else:
    print("Not found.")
