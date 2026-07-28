import re

with open('index.html', 'r') as f:
    content = f.read()

target = """          <a href="#about" class="magnetic-btn relative z-[2] flex items-center gap-3 bg-gradient-to-r from-primaryDim to-primaryBlue hover:from-primaryBlue hover:to-primaryBlue border border-outline rounded-full px-8 py-4 font-space text-xs uppercase tracking-widest text-black font-extrabold cursor-pointer hover:scale-105 active:scale-95 shadow-[0_0_20px_rgba(74,158,255,0.4)] transition-all duration-300" style="position: relative; z-index: 2;">
            <!-- Glow highlight anchor -->
            <div class="btn-glow-highlight absolute inset-0 pointer-events-none rounded-full bg-[radial-gradient(circle_at_var(--x)_var(--y),rgba(255,255,255,0.45)_0%,transparent_50%)] opacity-0 transition-opacity duration-300"></div>
            <span>Explore My World</span>
            <i data-lucide="arrow-down-right" class="w-4 h-4 text-black stroke-[2.5]"></i>
          </a>"""

replacement = """          <a href="#about" class="magnetic-btn relative z-[2] flex items-center gap-3 bg-gradient-to-r from-[#1a6fd4] to-[#4a9eff] hover:from-[#4a9eff] hover:to-[#4a9eff] border border-outline rounded-full px-8 py-4 font-space text-xs uppercase tracking-widest text-white font-extrabold cursor-pointer hover:scale-105 active:scale-95 shadow-[0_0_20px_rgba(74,158,255,0.4)] transition-all duration-300" style="position: relative; z-index: 2;">
            <!-- Glow highlight anchor -->
            <div class="btn-glow-highlight absolute inset-0 pointer-events-none rounded-full bg-[radial-gradient(circle_at_var(--x)_var(--y),rgba(255,255,255,0.45)_0%,transparent_50%)] opacity-0 transition-opacity duration-300"></div>
            <span>Explore My World</span>
            <i data-lucide="arrow-down-right" class="w-4 h-4 text-white stroke-[2.5]"></i>
          </a>"""

if target in content:
    content = content.replace(target, replacement)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
