import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace <span class="counter-num ..." data-target="2" data-format="standard">0</span>
content = content.replace('data-target="2"', 'data-target="3"')

with open('index.html', 'w') as f:
    f.write(content)
