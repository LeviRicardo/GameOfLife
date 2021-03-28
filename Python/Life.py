from random import choice as rd

def montar_tabuleiro(a=15,l=50):
    chances = 2
    possibilidades = [" " if i!= round(100/chances) else "#" for i in range(1, round(100/chances)+1)]
    tabuleiro = [ [] for i in range(a)]
    for linhas in range(len(tabuleiro)):
        tabuleiro[linhas] = "".join([rd(possibilidades) for i in range(l)])
    return(tabuleiro)   

def proximo_estagio(board=montar_tabuleiro()):
    




[print(i) for i in proximo_estagio()]