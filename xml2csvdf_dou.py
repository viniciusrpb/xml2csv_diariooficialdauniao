# -*- coding: utf-8 -*-
"""
Script Python que gera um arquivo .csv a partir de um conjunto de arquivos .xml relacionados com publicações do Diário Oficial da União.

Cada .xml possui uma úncica publicação (veja um exemplo na pasta dou_samples)

"""

import xml.etree.ElementTree as ET
import os
import pandas as pd

"""Nessa versão, colocamos diretamente os atributos do XML que queremos obter"""

xmls_path = "dou_samples/"
csv_filename = "corpus_dou.csv"

publicacoes_xmls = [publicacao_xml for publicacao_xml in os.listdir(xmls_path) if os.path.isfile(os.path.join(xmls_path,publicacao_xml))]

dicionario = {}

"""Criamos uma lista de listas, em que cada lista é uma instância relacionada com uma publicação que está em um arquivo XML"""

for publicacao_xml in publicacoes_xmls:

    xml_filename = xmls_path+publicacao_xml
            
    tree = ET.parse(xml_filename)
    root = mytree.getroot()
        
    for child in root:
        tag_xml = child.tag
        content_xml = child.attrib

    for attribute in content_xml:

      if attribute not in dicionario:
        dicionario[attribute] = []
        dicionario[attribute].append(content_xml[attribute])
      else:
        dicionario[attribute].append(content_xml[attribute])

    for x in myroot[0][0]:
      if x.tag not in dicionario:
        dicionario[x.tag] = []
        dicionario[x.tag].append(x.text)
      else:
        dicionario[x.tag].append(x.text)

"""Gera um DataFrame:"""

df = pd.DataFrame(dicionario)

"""Grava as publicações no DataFrame para o CSV"""

df.to_csv(csv_filename,sep=',',index=False)
