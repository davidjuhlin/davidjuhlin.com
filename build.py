#!/usr/bin/env python3
"""Builds the hosted site in docs/ (GitHub Pages) from index.html, the page
also used for the private preview: wraps it in a full HTML document with the
head, social preview and icon, and copies the images and résumé."""
import os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = open('index.html').read()
cut = src.index('<div class="wrap">')
head, body = src[:cut], src[cut:]
meta = '''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="canonical" href="https://davidjuhlin.com/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://davidjuhlin.com/">
<meta property="og:title" content="David Juhlin">
<meta property="og:description" content="I figure out what to build, and then I build it. Product manager and builder: Cuebright, Wicked Sidekick, and 10+ years in B2B SaaS and AI.">
<meta property="og:image" content="https://davidjuhlin.com/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
'''
os.makedirs('docs', exist_ok=True)
html = '<!doctype html>\n<html lang="en">\n<head>\n' + meta + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n'
open('docs/index.html', 'w').write(html)
for f in ['ws-hero.jpg', 'cb-site.jpg', 'cb-live.jpg', 'og.jpg', 'favicon.svg', 'resume.pdf']:
    shutil.copy(f, 'docs/' + f)
open('docs/.nojekyll', 'w').write('')
print('built docs/:', sorted(os.listdir('docs')))
