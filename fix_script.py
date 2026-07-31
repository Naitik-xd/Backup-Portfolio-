with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('''  <body class="relative">
      (function() {
        const savedTheme = localStorage.getItem('portfolio-theme');
        if (savedTheme === 'light') {
          document.body.classList.add('light-mode');
        }
      })();''', '''  <body class="relative">
    <script>
      (function() {
        const savedTheme = localStorage.getItem('portfolio-theme');
        if (savedTheme === 'light') {
          document.body.classList.add('light-mode');
        }
      })();
    </script>''')

with open('index.html', 'w') as f:
    f.write(content)
