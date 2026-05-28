import os

links = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            path = os.path.join(root, f).lstrip('./')
            links.append(f'<li><a href="{path}">{path}</a></li>')

html = '<h1>Docs</h1><ul>' + ''.join(links) + '</ul>'
open('index.html', 'w').write(html)
print('done')