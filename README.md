# XML2CSV de Publicações do Diário Oficial da União

Script que lê publicações do Diário Oficial da União (DOU) no formato XML e converte para DataFrame e Comma-Separated-Value (CSV).

## Scripts

Existem dois scripts:

- **xml2csvdf_dou.py**: converte *todos* os atributos do XMLs e as propriedades das tags para o arquivo .csv final;
- **xml2csvdf_dou_versao2.py**: converte apenas os atributos do XMLs e as propriedades das tags não ausentes para o arquivo .csv final;

Os arquivos .xml devem estar em uma pasta. Neste repositório, essa pasta é representada pelo folder "dou_samples", que já contém alguns arquivos .xml de publicações oficiais do Diário Oficial da União.

## Colaboradores do repositório

- youtch

## Referências

