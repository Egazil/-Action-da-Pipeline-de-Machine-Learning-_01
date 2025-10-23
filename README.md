1º é feito a leitura dos dados via **ucimlrepo ** --> Dessa forma não é necessário baixar a base de dados e deixar ela fixa
2º é feita toda a parte de processamento como separação da variavel alvo das demais e divisão da base de dados
3º Treinamento do modelo , no caso arvore de decisão e base de dados iris
4º Geração e salvamento do relatório em um txt
------------------------------------------------------
No github Actions
Verifica se o python está instalado e a versão instalada
Instala as pendencias que estão no arquivo requirements.txt
Executa o arquivo de treinamento que está em train.py
Dentro do arquivo train.py há uma parte que é gerado o relatorio e salvo como txt agora  será geraado como um Artifact
