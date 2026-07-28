import re

with open('api/ask-naitik.js', 'r') as f:
    content = f.read()

target = """Goals: Achieve big in AI, shape it not just use it, stay curious.
Contact: Naitik.270810@outlook.com
Rules: Keep answers concise. Use bullet points for lists instead of a single boring paragraph. Never make up information. End contact answers with his email.`;"""

replacement = """Goals: Achieve big in AI, shape it not just use it, stay curious.
Contact: Naitik.270810@outlook.com
Social Links:
- GitHub: https://github.com/Naitik-xd
- LinkedIn: https://www.linkedin.com/in/na1t1k
- X (Twitter): https://x.com/NA1T1Kxd
- Google Skills Profile: https://www.skills.google/public_profiles/38b0b619-88ee-4eea-845e-97512f415e2e
- Google Developer Profile: https://g.dev/na1t1k
Rules: Keep answers concise. Use bullet points for lists instead of a single boring paragraph. Never make up information. End contact answers with his email or provide relevant social links.`;"""

if target in content:
    content = content.replace(target, replacement)
    with open('api/ask-naitik.js', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
