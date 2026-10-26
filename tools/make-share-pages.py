#!/usr/bin/env python3
"""Make one small HTML page per post so shared links get their own preview.

Link previews (Facebook, Zalo, Messenger, LinkedIn...) ignore everything after "#",
so ttnganhuyen.com/#/words/x always shows the site thumbnail. A page at
ttnganhuyen.com/words/x carries that post's own og:image (its first photo, or its tab's
thumbnail when it has none) and sends visitors straight on to /#/words/x (old /blog/x pages stay and do the same).

Run from the repo root after adding or changing a post:  python3 tools/make-share-pages.py
"""
import html, os, re

SITE = 'https://www.ttnganhuyen.com'
DEFAULT_IMG = '/img/og-image.png'
SITE_NAME = 'Huyen Tran / Margot'
TAGLINE = 'consulting by day, blooming by night'

src = open('index.html', encoding='utf-8').read()


def page(path, title, desc, img, target, canon=None):
    e = lambda s: html.escape(s, quote=True)
    url, image = SITE + '/' + (canon or path), SITE + (img if img.startswith('/') else '/' + img)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="{'article' if '/' in path else 'website'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{image}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.ico">
<meta http-equiv="refresh" content="0; url=/{target}">
<script>location.replace('/{target}')</script>
</head>
<body><a href="/{target}">{e(title)}</a></body>
</html>
'''


def text(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def clip(s, n=160):
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'


def tab_img(tab):
    # each tab has its own thumbnail (img/og-<tab>.png, same look as the site one); posts without a photo use it too
    return '/img/og-%s.png' % tab if os.path.exists('img/og-%s.png' % tab) else DEFAULT_IMG


pages = {
    'me': ('Huyen Tran / Margot', TAGLINE, DEFAULT_IMG, '#/me'),
    'chapters': ('Chapters · Margot Tran', TAGLINE, tab_img('my-journey'), '#/chapters'),
    'cases': ('Cases · Margot Tran', TAGLINE, tab_img('use-cases'), '#/cases'),
    'words': ('Words · Margot Tran', TAGLINE, tab_img('blog'), '#/words'),
}

# Blog posts: <article class="post" id="post-ID"> … <h1> … first <img> … first <p>
for m in re.finditer(r'<article class="post" id="post-([\w-]+)"(.*?)</article>', src, re.S):
    pid, body = m.group(1), m.group(2)
    title = text(re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S).group(1))
    img = re.search(r'<img[^>]+src="([^"]+)"', body)
    p = re.search(r'<p[^>]*>(.*?)</p>', body, re.S)
    pages['words/' + pid] = (title + ' · Margot Tran', clip(text(p.group(1))) if p else TAGLINE,
                            img.group(1) if img and not img.group(1).startswith('data:') else tab_img('blog'), '#/words/' + pid)

# My journey: entries of the WORK array; an optional img: '…' field becomes the preview
for m in re.finditer(r"\{ id: '([\w-]+)', mark: '((?:[^'\\]|\\.)*)'.*?role: '((?:[^'\\]|\\.)*)'(.*?)\}(?=,?\s*(?:\{ id:|\]))", src, re.S):
    wid, mark, role, rest = m.group(1), m.group(2).replace("\\'", "'"), m.group(3).replace("\\'", "'"), m.group(4)
    img = re.search(r"\bimg: '([^']+)'", rest)
    p = re.search(r"p: \['((?:[^'\\]|\\.)*)'", rest)
    pages['chapters/' + wid] = (f'{mark} · {role} · Margot Tran', clip(text(p.group(1).replace("\\'", "'"))) if p else TAGLINE,
                                  img.group(1) if img else tab_img('my-journey'), '#/chapters/' + wid)

# links already shared under the old tab names (about, my-journey, use-cases, blog) keep working:
# those pages stay, point their canonical URL at the new name and send visitors to the new hash
LEGACY = {'me': ['about', 'profile'], 'chapters': ['my-journey'], 'cases': ['use-cases'], 'words': ['blog']}

for path, (title, desc, img, target) in pages.items():
    head, _, rest = path.partition('/')
    for out, canon in [(path, None)] + [(o + ('/' + rest if rest else ''), path) for o in LEGACY[head]]:
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        with open(out + '.html', 'w', encoding='utf-8') as f:
            f.write(page(out, title, desc, img, target, canon))
        print(f'{out}.html  ->  {img}')
