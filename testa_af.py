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
