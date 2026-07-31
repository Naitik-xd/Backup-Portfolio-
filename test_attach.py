with open('public/js/inline.js', 'r') as f:
    content = f.read()

content = content.replace('function attachEvents() {', 'function attachEvents() {\n    console.log("attachEvents called!");')

with open('public/js/inline.js', 'w') as f:
    f.write(content)
