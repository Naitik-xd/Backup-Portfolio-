import re

with open('api/ask-naitik.js', 'r') as f:
    content = f.read()

target = """Project: Bioluminescent Streetlight — vibe coded with Claude and Lovable, zero traditional code, live at https://bioluminescent-streetlights.lovable.app"""

replacement = """Projects: 
1. Bioluminescent Streetlight — vibe coded with Claude and Lovable, zero traditional code, live at https://bioluminescent-streetlights.lovable.app
2. Lumine-bay — a full-stack AI-powered salon booking platform built during a hackathon. It allows users to book appointments and consult with an AI stylist for an upgraded experience. Features a dedicated admin panel for salon owners. Live at https://luminae-bay.vercel.app/
3. Proof of Work — A SaaS platform designed for users to showcase their hackathon projects and participation certificates. Live at https://my-proof-of-work.vercel.app/"""

if target in content:
    content = content.replace(target, replacement)
    with open('api/ask-naitik.js', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
