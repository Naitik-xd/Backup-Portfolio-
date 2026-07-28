with open('api/ask-naitik.js', 'r') as f:
    content = f.read()

target = "- Google Developer Profile: https://g.dev/na1t1k"
replacement = "- Google Developer Profile: https://g.dev/na1t1k\n- Microsoft Learn: https://learn.microsoft.com/en-us/users/naitikagarwal-9821/"

if target in content:
    content = content.replace(target, replacement)
    with open('api/ask-naitik.js', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
