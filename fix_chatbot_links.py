import re

with open('index.html', 'r') as f:
    content = f.read()

target = """      function addMessage(text, type) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `chat-msg ${type}`;
        if (type === 'bot' && window.marked) {
          msgDiv.innerHTML = marked.parse(text);
        } else {
          msgDiv.textContent = text;
        }
        const msgContainer = document.getElementById('chat-messages');
        msgContainer.appendChild(msgDiv);
        msgContainer.scrollTop = msgContainer.scrollHeight;
      }"""

replacement = """      function addMessage(text, type) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `chat-msg ${type}`;
        if (type === 'bot' && window.marked) {
          msgDiv.innerHTML = marked.parse(text);
          const links = msgDiv.querySelectorAll('a');
          links.forEach(link => link.setAttribute('target', '_blank'));
        } else {
          msgDiv.textContent = text;
        }
        const msgContainer = document.getElementById('chat-messages');
        msgContainer.appendChild(msgDiv);
        msgContainer.scrollTop = msgContainer.scrollHeight;
      }"""

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
