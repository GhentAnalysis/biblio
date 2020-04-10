#!/usr/bin/env python3
import os, urllib.request, requests

webOfScienceExportFiles = ["2019.txt"]

def writePublication(lines):
  foundGhent = any(['Ghent' in line for line in lines])
  if foundGhent:
    collaboration, title, doi, journal, year, volume, issue, articleNumber, startPage, endPage = None, None, None, None, None, None, None, None, None, None
    searchSecondPartOfTitle = False
    for line in lines:
      if line.startswith('CA'): collaboration = line.replace('CA ', '').replace('\n','')
      if line.startswith('TI'): title         = line.replace('TI ', '').replace('\n','')
      if line.startswith('DI'): doi           = line.replace('DI ', '').replace('\n','')
      if line.startswith('JI'): journal       = line.replace('JI ', '').replace('\n','')
      if line.startswith('PY'): year          = line.replace('PY ', '').replace('\n','')
      if line.startswith('VL'): volume        = line.replace('VL ', '').replace('\n','')
      if line.startswith('IS'): issue         = line.replace('IS ', '').replace('\n','')
      if line.startswith('AR'): articleNumber = line.replace('AR ', '').replace('\n','')
      if line.startswith('BP'): startPage     = line.replace('BP ', '').replace('\n','')
      if line.startswith('EP'): endPage       = line.replace('EP ', '').replace('\n','')

      if searchSecondPartOfTitle and not line.startswith(' '): searchSecondPartOfTitle = False
      if searchSecondPartOfTitle: title += line.replace('   ', ' ').replace('\n', '')
      if line.startswith('TI'): searchSecondPartOfTitle = True

    if startPage and endPage: articleNumber = 'pages %s-%s' % (startPage, endPage)
    print('%s, "%s", %s%s (%s) %s%s, doi:%s' % (collaboration, title, journal, volume if volume else '', year, ('no. %s, ' % issue) if issue and issue!='1' else '', articleNumber if articleNumber else '', doi))

try:    os.makedirs('wosImports')
except: pass

for fileName in webOfScienceExportFiles:
  with open(fileName) as f:
    lines = []
    for line in f:
      if line=='\n': continue
      lines += [line]
      if line=='ER\n': # ER="End record", i.e. we can analyze the collected lines
        writePublication(lines)
        lines = lines[:2] # clean everything after the first two lines
