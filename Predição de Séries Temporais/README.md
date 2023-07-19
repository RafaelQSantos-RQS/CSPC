# Predição de séries temporais

## Campo
Predição de Séries Temporais

## Grupo de Pesquisa Afim
PIMAT

## Descrição
Implementar um método simples (https://en.wikipedia.org/wiki/MACD) que combina duas médias em janelas de tamanhos distintos para determinar se os valores da série vão aumentar ou diminuir no futuro próximo.

## Dificuldade / Passos
1. Leitura e manipulação de um arquivo .csv com as cotações em função do tempo, num período dado. Gerar o vetor Y(i), i=0,2,…,n-1, onde n é o número de pontos na série.
2. Implementar um algoritmo rápido para o cálculo da média móvel numa janela de tamanho definido w. Recebe um vetor de tamanho w com a cotação na janela.
3. Implementar um algoritmo que deslize duas janelas de tamanho w1 e w2, w1 < w2, ao longo dos pontos da série e calcule as médias em cada janela chamando a função criada acima.
   1. **DETALHE #1:** Se denotamos por “i” um ponto genérico na série, o vetor de entrada da função é formado por w cotações, sendo a última delas a cotação no ponto “i”, ou seja  Y[i]. 
   2. **DETALHE #2:** O primeiro ponto “i0 < n” que pode ser percorrido na série é o primero que permite calcular as duas médias.
4. Implementar a lógica de detecção de reversão de tendência conforme o método escolhido, que atribua a cada instante percorrido da série uma tendência +1 se a reversão for de descida para subida ou -1 em caso contrário. Nesse processo: (a) registrar os pontos onde ocorre reversão de tendência para sua plotagem posterior, (b) contar as reversões para descida (com o contador downRev) e para subida (com o contador upRev).
5. Plotar: (1) a série temporal com linha preta, (2) as duas médias com cores distintas (azul e vermelha),e  (3) os pontos de reversão de tendência com um * amarelo, encima da série temporal.
6. **OPCIONAL #1:** Registrar a tendência em cada ponto percorrido da série, para plotar depois em um subplot que tenha a série acima e o histórico da tendência embaixo, os dois “sincronizados” no tempo.
   1. **DETALHE:** perceber que a tendência começa em “i=i0” enquanto a série começa em “i=0"
7. **OPCIONAL #2:** Determinar, os valores máximo e mínimos da cotação entre duas reversões, sinalizando qual valor foi atingido primeiro, o mínimo ou o máximo.
8. **OPCIONAL #3:** Contar quantas vezes, quando a tendência era -1, o mínimo foi atingido primeiro (com o contador downOK) e da mesma forma, quando a tendência era +1, o máximo foi atingido primeiro (com o contador upOK).
9. **OPCIONAL #4:** Propor com usar downREv, downOK, upRev e upOK para avaliar a qualidade da predição usando esse método (MACD), com janelas de tamanho w1 e w2.