# SistemasLineares
Conjunto de notas com o apoio da biblioteca Lcapy

Estas notas foram escritas com base no curso que leciono ao curso de Engenharia Elétrica  na Universidade Regional de Blumenau-Santa Catarina-Brasil. 

Neste material a biblioteca Lcapy* (https://lcapy.readthedocs.io/en/latest/)  e o ecossistema Python são utilizados para simulação dos fenômenos pertinentes a teoria de sistemas lineares. 
Os notebooks podem ser renderizados aqui ou em nbviewer.org (https://nbviewer.org/). Para cada tema, há um notebook *.ipynb e uma versão *.html. 
Para executar em seu próprio computador, um sistema python científico deve ser instalado. Normalmente numpy, sympy, matplotlib, pandas, etc já vem previamente instalados nesses sistemas. Recomendo o uso de WinPython (https://winpython.github.io/). Para renderização das equações utilizadas no texto, o computador necessitará ter LateX instalado. MiKTeX  (https://miktex.org/) é uma distribuição que funciona muito bem em Windows e fará a renderização das equações de forma transparente.

Opcionalmente, os notebooks podem ser quase integralmente executados remotamente em serviços com o Binder (https://mybinder.org/). A maneira mais fácil de fazer isto é a partir da renderização de um notebook em nbviewer fazer a ligação direta com o Binder, disponível no alto da página. É necessário apenas incluir o comando de instalação de bibliotecas não encontradas, antes de sua importação. 

Exemplo: 

!pip install lcapy

 from lcapy import *
 
 etc..


*Hayes M. 2022. Lcapy: symbolic linear circuit analysis with Python. PeerJ Computer Science 8:e875 https://doi.org/10.7717/peerj-cs.875
