### [Calculadora Geométrica Bidimensional](Projetos/calculadoraGeo)
#### Objetivo:
Projetar um pequeno universo interativo dentro do qual seja possível registrar formas geométricas bidimensionais
úteis para verificações e cálculos simples.
#### Programa:
***Arquivos***
* [calcGeo.py](Projetos/calculadoraGeo/calcGeo.py): Arquivo responsável pela execução da calculadora
* [figurasGeometricas.py](Projetos/calculadoraGeo/MyLibs/figurasGeometricas.py): Arquivo com as classes das figuras geométricas
* [utils.py](Projetos/calculadoraGeo/MyLibs/utils.py): Arquivo com os utilitários usados para a configuração dos menus de seleção e organização de listas
* [Planejamento.txt](Projetos/calculadoraGeo/Planejamento.txt): Planejamento em pseudo-código das classes
* [casosTeste.txt](Projetos/calculadoraGeo/casosTeste.txt): Arquivo com entradas para teste e suas respectivas saídas esperadas

***Execução***

O programa apenas utiliza de biblitecas nativas do python3 sendo preciso apenas a instalacão desse, portanto para rodar o código
é necessário, estando dentro do diretório onde o arquivo calcGeo.py está localizado, executar o seguinte comando:
```
$ python3 calcGeo.py
```

Sua execução abre um menu com as figuras disponíveis para realização dos cálculos, podendo selecioná-las
a partir do número em azul a sua esquerda (1-5)

![Imagem 1](imagesRM/image_1.png)

Recebendo o número, o programa realça a opção selecionada e solicita a confirmação do usuário para proceder (s/n)

![Imagem 2](imagesRM/image_2.png)

Após a confirmação, é exibido um menu para o preenchimento das coordenadas, grifando a posição referente a entrada de dados

![Imagem 3](imagesRM/image_3.png)

Com as coordenadas completas, é perguntado se o usuário deseja trocar algum vértice (s/n), sua escolha podendo levá-lo a
um menu de troca onde a seleção é a mesma do menu inicial, solicitando uma confirmação em cada etapa

![Imagem 4](imagesRM/image_5.png)

Por fim é mostrado o resultado dos cálculos

![Imagem 5](imagesRM/image_6.png)
