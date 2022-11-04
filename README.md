# classyfier
Classificador de pontos para aprendizado de máquina utilizando geometria computacional.

# O projeto
_classyfier_ é um classificador binário simples, que utiliza algoritmos geométricos no plano 2D para calcular a envoltória convexa entre dois conjuntos de pontos e traçar uma reta entre eles, a fim de classificar eventuais novos pontos inseridos no plano. O _classyfier_ funciona em 4 etapas:
- Geração da envoltória convexa de duas classes de pontos.
- Varredura linear no plano para a validação da separabilidade linear entre as duas envoltórias (confirmar que as duas envoltórias não se intersectam).
- Encontrar os dois vértices mais próximos $vA$ e $vB$ entre as duas envoltórias.
- Traçar uma reta perpendicular a $vA$ e $vB$ de forma a dividir o plano entre as duas envoltórias.

Ao fim de execução do _classyfier_, para cada base de dados é gerado um modelo da seguinte forma (figura retirada da execução do algoritmo utilizando a base de dados _wine.dat_):

![wine_grafico](https://user-images.githubusercontent.com/73205375/200018590-a7d1f385-4a3a-47f0-baaf-53db8e22dabf.png)

# Implementação

## Geração da envoltória convexa ([convexHull.py](https://github.com/JoaoP-Silva/classyfier/blob/main/scripts/convexHull.py))
Primeiro, foi implementada a classe Node que seria usada para guardar os atributos x e y que seriam utilizados no nosso classificador, assim como sua label, que será utilizada para saber a qual classe esse Node específico pertence.
Esses nodes então são passados para o algoritmo de envoltória convexa. Foi utilizado o algoritmo descrito por Ronald Graham, referenciado pelo livro de Goodrich[1]. O algoritmo recebe uma lista de $n$ Nodes de uma mesma classe e, em tempo $O(n log (n))$ nos retorna uma lista dos Nodes que fazem parte da envoltória convexa daquela classe. Após este passo, nós temos duas listas de pontos que definem as duas diferentes envoltórias que serão utilizadas para calcular o nosso modelo.

## Varredura linear ([convexHullIntersect.py](https://github.com/JoaoP-Silva/classyfier/blob/main/scripts/convexHullIntersect.py))
Então é feita uma varredura linear para verificar a separabilidade linear entre os dados, ou seja, verifica-se que as envoltórias de cada classe não têm segmentos que se interceptam. Isso é feito, pois caso os dados não sejam linearmente separáveis, então não será possível criar o modelo e realizar as análises necessárias. A varredura linear é feita de acordo com o algoritmo referenciado por Cormen[2] e roda em tempo $O(n log (n))$.

## Encontrar os dois vértices mais próximos entre as duas envoltórias([Closest.py](https://github.com/JoaoP-Silva/classyfier/blob/main/scripts/Closest.py))
Assumindo então que os dados são linearmente separáveis, o próximo passo é calcular os pontos mais próximos entre as duas envoltórias. Isso foi feito utilizando a estrutura árvore-kd, descrita na seção 21.3 do livro Algorithm Desing and Applications[1], que possibilita consultas de um vizinho mais próximo em uma lista de tamanho $n$, no caso médio, em tempo $O(log (n))$. Como o custo da construção da estrutura para n pontos é $O(n log n)$ e são realizadas consultas para todos os pontos de ambas as envoltórias, o algoritmo implementado executa em tempo $O( m log (m) + n log (n))$ com $n$ e $m$ sendo a quantidade de pontos em cada uma das envoltórias. 

## Modelo classificador([classifier.py](https://github.com/JoaoP-Silva/classyfier/blob/main/scripts/classifier.py))
Assim, partimos para calcular nosso modelo, neste caso uma reta. Encontramos o ponto médio entre os dois pontos mais próximos calculados anteriormente e traçamos então a reta que passa perpendicularmente por esse ponto médio. Essa reta será o nosso modelo: os pontos que se encontrarem abaixo dela pertencem todos a uma mesma classe e os acimas a uma segunda classe. Este modelo é testado a partir de um conjunto de pontos separados previamente e, utilizando-se de algumas métricas, pode-se analisar o desempenho do modelo.

# Instruções de compilação e execução
O script [run.py](https://github.com/JoaoP-Silva/classyfier/blob/main/run.py) localizado no diretório raiz do projeto, itera sobre das bases de dados localizadas no arquivo _input.zip_ no diretório inputs e testa todas as combinações possíveis de atributos para tentar encontrar alguma que seja linearmente separável. Para o funcionamento correto do script, é necessário, além do python versão maior ou igual 3.8.8, instalar todas as bibliotecas utilizadas pelo programa. No terminal, digite:
``` pip install sortedcontainers functools numpy scipy ```

Após a instalação de todos os pacotes, verifique se o arquivo _input.zip_ no diretório inputs foi extraído dentro do próprio diretório. Com isso, dentro do diretório raiz do projeto, execute o script [run.py](https://github.com/JoaoP-Silva/classyfier/blob/main/run.py) através do comando:

```python run.py```

O resultado de todos os experimentos realizados será escrito em um arquivo _output.txt_ localizado na pasta raiz do projeto. A função _calculateMetrics()_, localizada no arquivo [classifier.py](https://github.com/JoaoP-Silva/classyfier/blob/main/scripts/classifier.py), calcula todas as métricas para análise do _classyfier_.

# Considerações finais
_classyfier_ é um repositório de estudo, o principal objetivo de implementar algoritmos geométricos e conseguir entender melhor o funcionamento prático de cada um deles foi alcançado com sucesso. Além disso, realizar este projeto foi interessante para compreender melhor métricas para análise de modelos (precição, recall e f1score), fora a experiência de desenvolvimento de software em grupo.
Para o futuro seria interessante a implementação da geração automática de gráficos e tabelas relacionadas com os resultados dos experimentos. 

# Referências
[1] GOODRICH, Michael; TAMASSIA, Roberto. Algorithm Design and Applications. 2014

[2] CORMEN, Thomas; LEISERSON, Charles. Introduction to Algorithms. 2009
