with open('public/js/inline.js', 'r') as f:
    content = f.read()

content = content.replace('function attachEvents() {\n    if (window._chatEventsAttached) return;\n    window._chatEventsAttached = true;\n    if (window._chatEventsAttached) return;\n    window._chatEventsAttached = true;', 'function attachEvents() {\n    if (window._chatEventsAttached) return;\n    window._chatEventsAttached = true;')

with open('public/js/inline.js', 'w') as f:
    f.write(content)
