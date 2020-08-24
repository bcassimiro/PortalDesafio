# Classificador de gênero
Autor: Bernardo Cassimiro Fonseca de Oliveira

Neste diretório, é desenvolvida uma análise dos dados dentro do contexto do processo seletivo da Portal. O objetivo aqui, além da análise, é a criação de uma ferramenta de classificação de gênero baseada nesses dados.

Neste repositório, existem as seguintes pastas/arquivos:
- Pasta "models" contendo um modelo responsável pela classificação.
- Arquivo "Análise de dados.ipynb" contendo a análise dos dados e a comparação entre classificadores.
- Arquivo "requirements.txt" contendo as bibliotecas necessárias para rodar a ferramenta.
- Arquivo "sex_predictor.py" contendo a aplicação que pode ser rodada do console.
- Arquivo "test_data_CANDIDATE.csv" contendo os dados a serem filtrados e utilizados para o treinamento do classificador.
- Arquivo "README.md", este arquivo.

As instruções para operar a ferramenta são as seguintes:
1) Clonar esse repositório para a sua interface
2) Acessar a pasta clonada pelo console do Anaconda
3) Criar um ambiente virtual no console do Anaconda utilizando o comando ```conda create --name env_name python=3.6```
4) Ativar o ambiente virtual com o comando ```conda activate env_name```
5) Instalar as bibliotecas necessárias para o funcionamento da ferramenta com o comando ```pip install -r requirements.txt```
6) Esperar a instalação das bibliotecas necessárias
7) Digite ```python sex_predictor.py newsample.csv```, em que "newsample.csv" é o arquivo a ser classificado
8) Espere o resultado da classificação e confira a saída do arquivo csv no diretório, contendo uma coluna com a classificação encontrada
