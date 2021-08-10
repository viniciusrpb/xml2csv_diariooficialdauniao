# -*- coding: utf-8 -*-
"""
Script Python que gera um arquivo .csv simplificado (com menos atributos em relação a versão principal) a partir de um conjunto de arquivos .xml relacionados com publicações do Diário Oficial da União.

Cada .xml possui uma úncica publicação (veja um exemplo na pasta dou_samples)

"""

import xml.etree.ElementTree as ET
import os
import pandas as pd

"""Nessa versão, colocamos diretamente os atributos do XML que queremos obter"""

xmls_path = "dou_samples/"
csv_filename = "corpus_dou.csv"

data_attributes = ['id','name', 'idOficio','pubName','artType','pubDate','artCategory','artSize','artNotes','numberPage','pdfPage','editionNumber','identifica','texto_publicacao']

publicacoes_xmls = [publicacao_xml for publicacao_xml in os.listdir(xmls_path) if os.path.isfile(os.path.join(xmls_path,publicacao_xml))]

lista = []

"""Criamos uma lista de listas, em que cada lista é uma instância relacionada com uma publicação que está em um arquivo XML"""

for publicacao_xml in publicacoes_xmls:
    instancia_dou = []
        
    xml_filename = xmls_path+publicacao_xml
            
    tree = ET.parse(xml_filename)
    root = tree.getroot()
            
    for child in root:
        tag_xml = child.tag
        content_xml = child.attrib

    for attribute in content_xml:
        if attribute != 'artClass' and attribute != 'highlightType' and attribute != 'highlightPriority' and attribute != 'highlight' and attribute != 'highlightimage' and attribute != 'highlightimagename' and attribute != 'artNotes':
            instancia_dou.append(content_xml[attribute])
                #print(attribute+" "+" "+dicionario[attribute])

    for x in root[0][0]:
        if x.tag == "Identifica":
            instancia_dou.append(x.text)
        elif x.tag == "Texto":
            instancia_dou.append(x.text)

    lista.append(instancia_dou)

"""Gera um DataFrame:"""

df = pd.DataFrame(lista,columns = data_attributes)

"""Grava as publicações no DataFrame para o CSV"""

df.to_csv(csv_filename,sep=',',index=False)
