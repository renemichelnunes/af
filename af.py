class estado():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class transicao():
    def __init__(self, de, para, elementos):
        self.de = de
        self.para = para
        self.elementos = elementos 

class AF():
    def __init__(self, alfabeto):
        self.alfabeto = alfabeto
        self.estados = []
        self.inicial = []
        self.final = []
        self.inalcancaveis = []
    
    def transicao(self, de, para, elementos):
        if de.tipo == 'i':
            if de.nome not in self.inicial:
                self.inicial.append(de.nome)
        elif de.tipo == 'f':
            if de.nome not in self.final:
                self.final.append(de.nome)
        if para.tipo == 'i':
            if para.nome not in self.inicial:
                self.inicial.append(para.nome)
        elif para.tipo == 'f':
            if para.nome not in self.final:
                self.final.append(para.nome)
        self.estados.append(transicao(de, para, elementos))
        self.final.sort()

    def __eh_afnd(self):
        #print('enumerando os estados')
        print('eh_afnd')
        estados = []
        for i in self.estados:
            if [i.de.nome] not in estados:
                estados.append([i.de.nome])
            if [i.para.nome] not in estados:
                estados.append([i.para.nome])
        estados.sort()
        #print(estados)

        #print('criando tabela vazia de transições')
        tabela = []
        for i in estados:
            linha = []
            for j in self.alfabeto:
                linha.append([])
            tabela.append(linha)
        #print(self.alfabeto)
        # imprime a tabela de transições
        #cont = 0
        #for i in tabela:
            #print('{}{}'.format(estados[cont][0], i))
            #cont += 1

        #print('analisando cada estado em sequencia a partir do inicial')
        #eh_afnd = False
        for i in estados:
            if len(i) > 0: # estados compostos
                for alfa in self.alfabeto:
                    temp = []
                    for est2 in i:
                        for est in self.estados:
                            if est.de.nome == est2:
                                for el in est.elementos:
                                    if el == alfa:
                                        #print('{} {} {}'.format(est.de.nome, est.para.nome, el))
                                        temp.append(est.para.nome)
                    temp.sort()
                    if temp != []:
                        #print('tabela[{}][{}]={}'.format(estados.index(i), self.alfabeto.index(alfa), temp))
                        tabela[estados.index(i)][self.alfabeto.index(alfa)] = temp
                    if len(temp) > 1 and temp not in estados:
                        return True
        return False

    def testa(self, palavra):
        if self.__eh_afnd():
            self.__afnd()
        #print('enumerando os estados')
        estados = []
        for i in self.estados:
            if [i.de.nome] not in estados:
                estados.append([i.de.nome])
            if [i.para.nome] not in estados:
                estados.append([i.para.nome])
        estados.sort()
        print('estados {}'.format(estados))
        print('inicial {}'.format(self.inicial))
        print('finais {}'.format(self.final))
        print('inalcançáveis {}'.format(self.inalcancaveis))
        print('alfabeto {}'.format(self.alfabeto))

        #print('criando tabela vazia de transições')
        tabela = []
        for i in estados:
            linha = []
            for j in self.alfabeto:
                linha.append([])
            tabela.append(linha)

        
        # imprime a tabela de transições
        cont = 0
        for i in tabela:
            #print('{}{}'.format(estados[cont][0], i))
            cont += 1

        #print('analisando cada estado em sequencia a partir do inicial')
        #eh_afnd = False
        for i in estados:
            if len(i) > 0: # estados compostos
                for alfa in self.alfabeto:
                    temp = []
                    for est2 in i:
                        for est in self.estados:
                            if est.de.nome == est2:
                                for el in est.elementos:
                                    if el == alfa:
                                        #print('{} {} {}'.format(est.de.nome, est.para.nome, el))
                                        temp.append(est.para.nome)
                    temp.sort()
                    if temp != []:
                        #print('tabela[{}][{}]={}'.format(estados.index(i), self.alfabeto.index(alfa), temp))
                        tabela[estados.index(i)][self.alfabeto.index(alfa)] = temp
        
        tabela2 = tabela.copy()
        for i in range(0, len(estados)):
            for j in range(0, len(self.alfabeto)):
                if tabela[i][j] != []:
                    tabela2[i][j] = estados.index(tabela[i][j])
        
        #for i in tabela2:
        #    print(i)

        colunas = []
        for i in range(0, len(self.alfabeto)):
            colunas.append(i)

        pal = palavra
        linha = 0
        coluna = 0
        for i in self.alfabeto:
            pal = pal.replace(i, str(self.alfabeto.index(i)))
        
        print("Palavra: {}".format(palavra))
        lin = 0
        lina = 0
        for i in pal:
            try:
                lina = lin
                print("{}={}".format(estados[lin][0], self.alfabeto[int(i)]))
                #print("{} {}".format(lin, int(i)))
                lin = tabela2[lin][int(i)]
                if lin == []:
                    break
                else:
                    lina = lin
            except Exception:
                print('símbolo [{}] não faz parte do alfabeto, rejeitada'.format(i))
                return

        if lin != [] and set(self.final).intersection(estados[lin]):
            print("estado final {} aceito".format(estados[lin][0]))
        else:
            print("estado {} rejeitado".format(estados[lina][0]))

    def __afnd(self):
        print('afnd')
        print('enumerando os estados')
        estados = []
        for i in self.estados:
            if [i.de.nome] not in estados:
                estados.append([i.de.nome])
            if [i.para.nome] not in estados:
                estados.append([i.para.nome])
        estados.sort()
        print(estados)

        print('criando tabela vazia de transições')
        tabela = []
        for i in estados:
            linha = []
            for j in self.alfabeto:
                linha.append([])
            tabela.append(linha)
        print(self.alfabeto)
        # imprime a tabela de transições
        cont = 0
        for i in tabela:
            print('{}{}'.format(estados[cont][0], i))
            cont += 1

        print('analisando cada estado em sequencia a partir do inicial')
        for i in estados:
            if len(i) > 0: # estados compostos
                for alfa in self.alfabeto:
                    temp = []
                    for est2 in i:
                        for est in self.estados:
                            if est.de.nome == est2:
                                for el in est.elementos:
                                    if el == alfa:
                                        print('{} {} {}'.format(est.de.nome, est.para.nome, el))
                                        if est.para.nome not in temp:
                                            temp.append(est.para.nome)
                    temp.sort()
                    if temp != []:
                        print('tabela[{}][{}]={}'.format(estados.index(i), self.alfabeto.index(alfa), temp))
                        tabela[estados.index(i)][self.alfabeto.index(alfa)] = temp
                    if len(temp) > 1 and temp not in estados:
                        print('novo estado! {}'.format(temp))
                        estados.append(temp) # acrescente na lista de estados
                        tabela.append([[], [], [], []]) # adicione uma linha na tabela de transições
            
    
        print('lista de estados atualizada')
        print(estados)
        # imprime a tabela de transições
        print('tabela de transições atualizada')
        cont = 0
        for i in tabela:
            print('q{} {}'.format(cont, i))
            cont += 1

        af = AF(self.alfabeto)
        print('este autômato é não determinístico')
        self.imprime_automato()
        print()
        for i in range(0, len(estados)):
            for j in range(0, len(self.alfabeto)):
                if tabela[i][j] != []:
                    if i == 0: # o estado inicial é o primeiro estado da lista de estados
                        de = estado('q{}'.format(i), 'i')
                        if set(self.final).intersection(estados[estados.index(tabela[i][j])]):
                            para = estado('q{}'.format(estados.index(tabela[i][j])), 'f')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
                        else:
                            para = estado('q{}'.format(estados.index(tabela[i][j])), '')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
                    elif set(self.final).intersection(estados[i]):
                        de = estado('q{}'.format(i), 'f')
                        if set(self.final).intersection(estados[estados.index(tabela[i][j])]):
                            para = estado('q{}'.format(estados.index(tabela[i][j])), 'f')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
                        else:
                            para = estado('q{}'.format(estados.index(tabela[i][j])), '')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
                    else:
                        de = estado('q{}'.format(i), '')
                        if set(self.final).intersection(estados[estados.index(tabela[i][j])]):
                            para = estado('q{}'.format(estados.index(tabela[i][j])), 'f')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
                        else:
                            para = estado('q{}'.format(estados.index(tabela[i][j])), '')
                            af.transicao(de, para, [self.alfabeto[j]])
                            #print('{}{}->{}{}={}'.format(de.nome, de.tipo, para.nome, para.tipo, self.alfabeto[j]))
        self.alfabeto = af.alfabeto.copy()
        self.inicial = af.inicial.copy()
        self.final = af.final.copy()
        self.final.sort(key=lambda x: int(x[1:]))
        self.estados = af.estados.copy()
        #print('enumerando os estados')
        estados2 = []
        for i in af.estados:
            if [i.de.nome] not in estados2:
                estados2.append([i.de.nome])
            if [i.para.nome] not in estados2:
                estados2.append([i.para.nome])
        estados2.sort()
        #print(estados2)

        inalcancaveis = []
        for i in estados2:
            achou = False
            for j in af.estados:
                if i[0] == j.para.nome:
                    achou = True
            if not achou and i != estados2[0] and i[0] not in inalcancaveis:
                inalcancaveis.append(i[0])

        inalcancaveis.sort()
        self.inalcancaveis = inalcancaveis
        #print('estados inalcançáveis {}'.format(inalcancaveis))

        #print('retirando do automato')
        #temp = []
        #for i in af.estados:
        #    if i.de.nome not in inalcancaveis:
        #        temp.append(i)
        #af.estados = temp
        print('convertido para determinístico')
        self.imprime_automato()
        print()

    def imprime_automato(self):
        for estado in self.estados:
            print("{}->{} {}".format(estado.de.nome, estado.para.nome, estado.elementos))
