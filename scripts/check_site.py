from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=list(root.glob('*.html'))
errors=[]
for f in files:
    html=f.read_text(encoding='utf-8')
    for token in ['<title>','name="description"','rel="canonical"','application/ld+json','<h1']:
        if token not in html: errors.append(f'{f.name}: missing {token}')
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(('http','mailto:','tel:','#')): continue
        target=root/href.split('#')[0]
        if href and not target.exists(): errors.append(f'{f.name}: broken link {href}')
print('html_files',len(files))
print('errors',len(errors))
for e in errors: print(e)
sys.exit(1 if errors else 0)
