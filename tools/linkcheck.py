#!/usr/bin/env python3
"""Validate every internal link, anchor, and asset reference in the KONNEKT docs.

Exits non-zero if anything is broken, so it can gate CI.

Checks:
  - relative links resolve to a file, or a directory containing README.md
  - heading anchors exist, including GitBook's "id-" prefix on digit-initial
    headings and explicit <a id="..."> anchors
  - image / file asset paths exist on disk
  - absolute docs.konnekt.io self-links resolve to a real page and anchor
    (these should be relative .md paths - see the style guide)
  - GitHub blob URLs used as images (they serve HTML, not the image)

External http(s) links are not checked here; that needs network access.

Usage:  python3 tools/linkcheck.py
"""
import glob, os, re, sys, urllib.parse

ROOT='docs'; HOST='docs.konnekt.io'

def slug(h):
    h=h.strip()
    h=re.sub(r'`([^`]*)`',r'\1',h)
    h=re.sub(r'\*+([^*]*)\*+',r'\1',h)
    h=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',h)
    h=re.sub(r'&#x[0-9a-fA-F]+;|&\w+;','',h)
    h=h.lower()
    h=re.sub(r'[/\\_&+]',' ',h)          # separators become spaces -> hyphens
    h=re.sub(r'[^a-z0-9.\s-]','',h)
    h=re.sub(r'\s+','-',h.strip())
    h=re.sub(r'-{2,}','-',h).strip('-')
    if h and h[0].isdigit(): h='id-'+h      # GitBook prefixes digit-initial anchors
    return h

headings={}
for f in glob.glob(f'{ROOT}/**/*.md',recursive=True):
    hs=set(); fence=False
    for line in open(f,encoding='utf-8'):
        if line.lstrip().startswith('```'): fence=not fence; continue
        if fence: continue
        for a in re.findall(r'id="([^"]+)"',line):   # GitBook explicit anchors
            hs.add(a.lower())
        m=re.match(r'(#{1,6})\s+(.*)',line)
        if m:
            txt=re.sub(r'<a\b[^>]*>.*?</a>|<a\b[^>]*/?>','',m.group(2))
            hs.add(slug(txt))
    headings[os.path.normpath(f)]=hs

def extract(line):
    out=[]
    # markdown links: (<path with spaces>) or (path)
    for m in re.finditer(r'\]\(\s*(?:<([^>]*)>|([^)\s]+))',line):
        out.append((m.group(1) or m.group(2)).strip())
    for m in re.finditer(r'(?:src|href)="([^"]*)"',line): out.append(m.group(1).strip())
    for m in re.finditer(r'{%\s*(?:file|embed)\s+(?:src|url)="([^"]*)"',line): out.append(m.group(1).strip())
    return [t for t in out if t]

def resolve(src,tgt):
    p=os.path.normpath(os.path.join(os.path.dirname(src),tgt)) if tgt else os.path.normpath(os.path.dirname(src))
    if os.path.isfile(p): return p,''
    if os.path.isdir(p):
        r=os.path.join(p,'README.md')
        return (os.path.normpath(r),'') if os.path.isfile(r) else (None,'directory has no README.md')
    if not p.endswith('.md') and os.path.isfile(p+'.md'): return os.path.normpath(p+'.md'),''
    return None,'file does not exist'

def pub(u):
    path=urllib.parse.urlparse(u).path.strip('/')
    if not path: return os.path.normpath(os.path.join(ROOT,'README.md'))
    for c in (os.path.join(ROOT,path+'.md'),os.path.join(ROOT,path,'README.md')):
        if os.path.isfile(c): return os.path.normpath(c)
    return None

broken=[]
for f in sorted(glob.glob(f'{ROOT}/**/*.md',recursive=True)):
    fn=os.path.normpath(f)
    for i,line in enumerate(open(f,encoding='utf-8').read().split('\n'),1):
        for t in extract(line):
            if t.startswith(('mailto:','tel:','data:')): continue
            if t.startswith('#'):
                if t[1:] and t[1:].lower() not in headings[fn]:
                    broken.append((fn,i,t,'same-page anchor not found'))
                continue
            if re.match(r'^https?://',t):
                if HOST in t:
                    p=pub(t)
                    if p is None: broken.append((fn,i,t,'published self-link: page does not exist'))
                    else:
                        fr=urllib.parse.urlparse(t).fragment
                        if fr and fr.lower() not in headings.get(p,set()):
                            broken.append((fn,i,t,f'published self-link: anchor missing in {p}'))
                elif 'github.com' in t and '/blob/' in t and re.search(r'\.(png|jpe?g|webp|gif|svg)$',t,re.I):
                    broken.append((fn,i,t,'GitHub blob URL used as image'))
                continue
            tgt,_,fr=t.partition('#')
            p,note=resolve(f,tgt)
            if p is None: broken.append((fn,i,t,note)); continue
            if fr and p.endswith('.md') and fr.lower() not in headings.get(p,set()):
                broken.append((fn,i,t,f'anchor missing in {p}'))

for fn,i,t,w in broken:
    print(f'{fn}:{i}\n    {t}\n    -> {w}')
print(f'\n{len(headings)} files checked  |  BROKEN: {len(broken)}')
sys.exit(1 if broken else 0)
