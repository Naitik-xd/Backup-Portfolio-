import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove onclick="toggleChat()"
content = content.replace('onclick="toggleChat()"', '')

# Remove onclick="sendSuggested(...)"
# They are:
# onclick="sendSuggested('What can Naitik do?')"
# onclick="sendSuggested('His projects 🚀')"
# onclick="sendSuggested('Top achievements')"
# onclick="sendSuggested('Contact him')"

content = content.replace('onclick="sendSuggested(\'What can Naitik do?\')"', 'id="chip-1"')
content = content.replace('onclick="sendSuggested(\'His projects 🚀\')"', 'id="chip-2"')
content = content.replace('onclick="sendSuggested(\'Top achievements\')"', 'id="chip-3"')
content = content.replace('onclick="sendSuggested(\'Contact him\')"', 'id="chip-4"')

content = content.replace('onkeypress="handleEnter(event)"', '')
content = content.replace('onclick="sendChatMessage()"', '')

with open('index.html', 'w') as f:
    f.write(content)
