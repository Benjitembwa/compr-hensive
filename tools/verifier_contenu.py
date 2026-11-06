#!/usr/bin/env python3
"""Vérifie la structure et les données de l'application, sans installer de dépendances."""
import pathlib,json,sys
R=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((R/'data/lessons.json').read_text(encoding='utf8'))
lessons=d['lessons'];errors=[]
if len(lessons)!=30: errors.append('La liste doit contenir 30 leçons.')
if [l.get('id') for l in lessons]!=list(range(1,31)):errors.append('Les identifiants doivent être 1 à 30.')
for l in lessons:
 i=l.get('id');w=l.get('vocab',[]);g=l.get('grammar',[]);dialogs=l.get('dialogs',[])
 if len(w)<15:errors.append(f'Leçon {i}: vocabulaire insuffisant')
 if len(g)<3:errors.append(f'Leçon {i}: il faut au moins trois notions')
 if len(dialogs)!=2:errors.append(f'Leçon {i}: deux dialogues requis')
 for x in w:
  if not all(x.get(k) for k in ('zh','py','fr')):errors.append(f'Leçon {i}: entrée de vocabulaire incomplète')
 for x in g:
  if not all(x.get(k) for k in ('title','formula','explanation','zh','py','fr','warning')):errors.append(f'Leçon {i}: règle de grammaire incomplète')
 for dialog in dialogs:
  if len(dialog.get('lines',[]))<4:errors.append(f'Leçon {i}: dialogue trop court')
  if not {'A','B'}.issubset({x['speaker'] for x in dialog.get('lines',[]) }):errors.append(f'Leçon {i}: dialogue sans deux interlocuteurs A et B')
  for x in dialog['lines']:
   if not all(x.get(k) for k in ('speaker','zh','py','fr')):errors.append(f'Leçon {i}: réplique incomplète')
if errors:
 for err in errors: print('ERREUR:',err)
 sys.exit(1)
print('VALIDATION OK')
print('Leçons',len(lessons))
print('Entrées de vocabulaire',sum(len(l['vocab']) for l in lessons))
print('Fiches de grammaire',sum(len(l['grammar']) for l in lessons))
print('Dialogues',sum(len(l['dialogs']) for l in lessons))
print('Répliques',sum(len(di['lines']) for l in lessons for di in l['dialogs']))
print('Phrases de lecture',sum(len(t['lines']) for l in lessons for t in l['readings']))
