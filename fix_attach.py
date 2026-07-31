with open('public/js/inline.js', 'r') as f:
    content = f.read()

# Add deduplication guard to attachEvents
guard = """function attachEvents() {
    if (window._chatEventsAttached) return;
    window._chatEventsAttached = true;"""

content = content.replace('function attachEvents() {\n    console.log("attachEvents called!");', guard)
content = content.replace('function attachEvents() {', guard)

with open('public/js/inline.js', 'w') as f:
    f.write(content)
