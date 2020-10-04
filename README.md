# af
AF é uma classe em python usada para criar e testar autômatos finitos determinísticos e não-determinísticos. Para criar um autômato, primeiro importe a classe, defina a instância do autômato, crie os estados e defina as transições. Use-a com a versão 3 do python.

# Como importar a classe
from af import AF, estado

# Definindo o autômato
O autômato AF é instanciado passando uma lista com os símbolos do alfabeto separados por vírgula


af = AF(['a', 'b', ...])

# Criando os estados
Um estado consiste do nome e o tipo, se é inicial 'i', final 'f' ou simples ''. Não há restrição quanto a nomenclatura.


a = estado('q0', 'i')

b = estado('q1', '')

c = estado('C', 'f')

x = estado('nome','tipo')


# Definindo as transações
As transações são definidas assim: estado de origem, estado de destino e lista de símbolos da transição.


af.transicao(q0, q1, ['a', 'b', ...])


No caso de loops ou transação com vários símbolos, Você pode definir de duas formas:


Com apenas um símbolo:

af.transicao(q0, q0, ['a'])


Com vários símbolos:

af.transicao(q0, q0, ['a', 'b', ...])


Ou separadamente para cada símbolo:

af.transicao(q0, q0, ['a'])
af.transicao(q0, q0, ['b'])
af.transicao(q0, q0, ['n'])

# Métodos
O autômato possui dois métodos, 'imprime_automato()' mostra uma lista com as transições, e 'testa(palavra)' é usado para verificar se a palavra faz parte da linguagem processada pelo autômato ex:


Imprime o autômato:


af.imprime_automato()

q0->q0 ['a']

q0->q1 ['a']

q1->q2 ['b']

q1->q3 ['b']

q1->q5 ['b']

q2->q1 ['a']


Testa uma palavra:


af.testa('abc')

q0=a

q7=b

q8=c


estado final q9 aceito


af.testa('abbbbcd')

q0=a

q7=b

q8=b


estado q8 rejeitado


# Exemplo prático
Autômato que reconhece palavras terminadas em 'b':



from af import AF, estado


af = AF(['a', 'b'])

a = estado('A', 'i')

b = estado('B', '')

c = estado('C', 'f')



af.transicao(a, b, ['a'])

af.transicao(a, c, ['b'])

af.transicao(b, b, ['a'])

af.transicao(b, c, ['b'])

af.transicao(c, b, ['a'])

af.transicao(c, c, ['b'])


af.imprime_automato()

af.testa('ababbbabababab')


Resultado:


A->B ['a']

A->C ['b']

B->B ['a']

B->C ['b']

C->B ['a']

C->C ['b']

estados [['A'], ['B'], ['C']]

inicial ['A']

finais ['C']

alfabeto ['a', 'b']

Palavra: ababbbabababab

A=a

B=b

C=a

B=b

C=b

C=b

C=a

B=b

C=a

B=b

C=a

B=b

C=a

B=b

estado final C aceito


No caso de um autômato não determinístico, o método 'testa(palavra)' detecta, converte e atualiza para determinístico, e depois prosegue com teste da palavra. 


from af import AF, estado


af = AF(['a', 'b', 'c', 'd'])

q0 = estado('q0', 'i')

q1 = estado('q1', '')

q2 = estado('q2', '')

q3 = estado('q3', '')

q4 = estado('q4', 'f')

q5 = estado('q5', 'f')

q6 = estado('q6', 'f')


af.transicao(q0, q0, ['a'])

af.transicao(q0, q1, ['a'])

af.transicao(q1, q2, ['b'])

af.transicao(q1, q3, ['b'])

af.transicao(q1, q5, ['b'])

af.transicao(q2, q1, ['a'])

af.transicao(q3, q4, ['c'])

af.transicao(q4, q4, ['c'])

af.transicao(q5, q6, ['c'])

af.transicao(q6, q6, ['d'])


af.testa('ab')

print()

af.testa('abc')

print()

af.testa('abcd')

print()

af.testa('abbbbcd')


Resulta em:


este autômato é não determinístico

q0->q0 ['a']

q0->q1 ['a']

q1->q2 ['b']

q1->q3 ['b']

q1->q5 ['b']

q2->q1 ['a']

q3->q4 ['c']

q4->q4 ['c']

q5->q6 ['c']

q6->q6 ['d']


convertido para determinístico

q0->q7 ['a']

q1->q8 ['b']

q2->q1 ['a']

q3->q4 ['c']

q4->q4 ['c']

q5->q6 ['c']

q6->q6 ['d']

q7->q7 ['a']

q7->q8 ['b']

q8->q1 ['a']

q8->q9 ['c']

q9->q4 ['c']

q9->q6 ['d']


estados [['q0'], ['q1'], ['q2'], ['q3'], ['q4'], ['q5'], ['q6'], ['q7'], ['q8'], ['q9']]

inicial ['q0']

finais ['q4', 'q5', 'q6', 'q8', 'q9']

alfabeto ['a', 'b', 'c', 'd']

Palavra: ab

q0=a

q7=b

estado final q8 aceito


estados [['q0'], ['q1'], ['q2'], ['q3'], ['q4'], ['q5'], ['q6'], ['q7'], ['q8'], ['q9']]

inicial ['q0']

finais ['q4', 'q5', 'q6', 'q8', 'q9']

alfabeto ['a', 'b', 'c', 'd']

Palavra: abc

q0=a

q7=b

q8=c

estado final q9 aceito


estados [['q0'], ['q1'], ['q2'], ['q3'], ['q4'], ['q5'], ['q6'], ['q7'], ['q8'], ['q9']]

inicial ['q0']

finais ['q4', 'q5', 'q6', 'q8', 'q9']

alfabeto ['a', 'b', 'c', 'd']

Palavra: abcd

q0=a

q7=b

q8=c

q9=d

estado final q6 aceito


estados [['q0'], ['q1'], ['q2'], ['q3'], ['q4'], ['q5'], ['q6'], ['q7'], ['q8'], ['q9']]

inicial ['q0']

finais ['q4', 'q5', 'q6', 'q8', 'q9']

alfabeto ['a', 'b', 'c', 'd']

Palavra: abbbbcd

q0=a

q7=b

q8=b

estado q8 rejeitado

