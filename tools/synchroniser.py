#!/usr/bin/env python3
"""Synchronise data/lessons.json vers data/lessons.js, sans dépendance externe."""
import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
src=ROOT/'data'/'lessons.json'
dst=ROOT/'data'/'lessons.js'
try:
 data=json.loads(src.read_text(encoding='utf-8'))
assert len(data.get('lessons',[]))==30
assert [x['id'] for x in data['lessons']]==list(range(1,31))
dst.write_text('window.MANDARIN_LESSONS = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
print('Synchronisation réussie :',len(data['lessons']),'leçons →',dst)
