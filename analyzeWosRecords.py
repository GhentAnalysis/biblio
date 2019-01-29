#!/usr/bin/env python3
import os, urllib.request, requests

webOfScienceExportFiles = ["allWosExports.txt"]

# Use arxiv because the fucking Elsevier website makes it too difficult to download stuff
def getLinkFromArxiv(doi):
  r = requests.get('https://arxiv.org/search/?query=' + doi.replace('/', '%2F') + '&searchtype=doi')
  for line in r.text.split('\n'):
    if 'https://arxiv.org/pdf' in line: return line.split('a href="')[-1].split('"')[0]
  return None

def getPaper(doi, outFile):
  if os.path.exists(outFile): return
  link = None
  if 'PhysRevLett'                         in doi: link = 'https://journals.aps.org/prl/pdf/' + doi
  elif 'PhysRevD'                          in doi: link = 'https://journals.aps.org/prd/pdf/' + doi
  elif 'PhysRevC'                          in doi: link = 'https://journals.aps.org/prc/pdf/' + doi
  elif 'JHEP'                              in doi: link = 'https://link.springer.com/content/pdf/' + doi.replace('/', '%2F')
  elif 'jhep'                              in doi: link = 'https://link.springer.com/content/pdf/' + doi.replace('/', '%2F')
  elif 'epjconf'                           in doi: link = getLinkFromArxiv(doi)
  elif 'epjc'                              in doi: link = 'https://link.springer.com/content/pdf/' + doi
# elif '10.1038/nature14474'               == doi: link = 'https://www.nature.com/nature/journal/v522/n7554/pdf/nature14474.pdf' # Add special cases like this
  elif 'physletb'                          in doi: link = getLinkFromArxiv(doi)
# else:                                            link = 'https://iopscience.iop.org/article/' + doi + '/pdf'  # for the ones on IOP science, but they block your IP if you download too much
  else:                                            link = getLinkFromArxiv(doi)
  if link: 
    try:    urllib.request.urlretrieve(link, outFile)
    except: print('Problem with link ' + link)
  else:     print('Do not know what to do with ' + doi)
  


def writeSingleRecord(outFile, lines):
  foundGhent = any(['Ghent' in line for line in lines])
  if foundGhent:
    with open(outFile, 'w') as out:
      for line in lines:
        if line.startswith('DI'): getPaper(line.split()[-1], outFile.replace('.txt', '.pdf'))
        out.write(line)
  return foundGhent

try:    os.makedirs('wosImports')
except: pass

i = 0
for fileName in webOfScienceExportFiles:
  with open(fileName) as f:
    lines = []
    for line in f:
      if line=='\n': continue
      lines += [line]
      if line=='ER\n': 
        if writeSingleRecord('wosImports/CMS-paper-' + str(i).zfill(4) + '.txt', lines): i+=1
        lines = lines[:2] # clean everything after the first two lines
