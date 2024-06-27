# Prova final da matéria de Engenharia Médica.
Projeto escrito por Christopher Akira França Maekawa para a avaliação dos conteúdos oferecidos na matéria de Engenharia Médica, ministrada pelo professor Jose Jair Alves Mendes Junior.

## Proposta 
A prova é o desenvolvimento de algoritmo, usando os sinais brutos, para determinar o valor da pressão sanguínea.

## Resultado obtido
Foi possível utilizar os dados contidos no arquivo CSV para estimar os valores de pressão sanguínea máxima e mínima, além de criar um gráfico para melhor visualização dos dados.

## Clone do repositório
Primeiro, é necessário clonar o repositório para uma pasta de sua escolha:
```bash
git clone https://github.com/chrisakira/prova_eng_medica.git
```
Ou realizar o download do repositório diretamente do GitHub em formato zip e fazer a extração manual para a pasta de destino.

## Instalação
Para realizar a instalação, é necessária a versão do Python 3.10 ou superior, assim como o pip.

### Intalação ambiente windows 
Para ambiente windows, basta instalar a versão desejada diretamente no site oficial do python [Python](https://www.python.org/downloads/).

### Instalação ambiente linux
Para ambiente linux, instale o python e o pip utilizando os seguintes comandos:
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Instalação das bibliotecas
Para instalar as bibliotecas utilizadas neste projeto, abra o terminal na raiz do projeto e execute o seguinte comando:
```bash
pip install -r requirements.txt
```

## Execução
Para executar o código, insira o seu arquivo .csv a ser utilizado na raiz do projeto e, em seguida, execute o seguinte comando:
```bash
python3 main.py
```

O resultado será gerado na pasta raiz do projeto com o nome de "plot.png", contendo as informações solicitadas no enunciado do projeto.