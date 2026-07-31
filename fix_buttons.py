import re

with open('index.html', 'r') as f:
    content = f.read()

# sound toggle
content = content.replace('id="sound-toggle"', 'id="sound-toggle" aria-label="Toggle Sound"')
# theme toggle
content = content.replace('id="theme-toggle"', 'id="theme-toggle" aria-label="Toggle Theme"')
# modal close
content = content.replace('id="modal-close-trigger"', 'id="modal-close-trigger" aria-label="Close Modal"')
# chat send
content = content.replace('id="chat-send"', 'id="chat-send" aria-label="Send Chat Message"')

# chat widget bubble - add role="button" and aria-label
content = content.replace('id="chat-widget-bubble" onclick', 'id="chat-widget-bubble" role="button" aria-label="Open Chat" onclick')

# chat close - add role="button" and aria-label
content = content.replace('class="chat-close" onclick', 'class="chat-close" role="button" aria-label="Close Chat" onclick')

# social links - add aria-label
content = content.replace('href="https://github.com/Naitik-xd"', 'href="https://github.com/Naitik-xd" aria-label="GitHub"')
content = content.replace('href="https://www.linkedin.com/in/na1t1k"', 'href="https://www.linkedin.com/in/na1t1k" aria-label="LinkedIn"')
content = content.replace('href="https://x.com/NA1T1Kxd"', 'href="https://x.com/NA1T1Kxd" aria-label="X Twitter"')
content = content.replace('href="https://www.skills.google/public_profiles/38b0b619-88ee-4eea-845e-97512f415e2e"', 'href="https://www.skills.google/public_profiles/38b0b619-88ee-4eea-845e-97512f415e2e" aria-label="Google Skills"')
content = content.replace('href="https://g.dev/na1t1k"', 'href="https://g.dev/na1t1k" aria-label="Google Developer"')
content = content.replace('href="https://learn.microsoft.com/en-us/users/naitikagarwal-9821/"', 'href="https://learn.microsoft.com/en-us/users/naitikagarwal-9821/" aria-label="Microsoft Learn"')

# Add aria-label to sidebar dots
content = content.replace("dotBtn.setAttribute('data-target-id', sec.id);", "dotBtn.setAttribute('data-target-id', sec.id);\n          dotBtn.setAttribute('aria-label', 'Scroll to ' + sec.id);")

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
