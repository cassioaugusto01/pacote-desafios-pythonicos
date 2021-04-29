"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
1 - adicione 'ing' no seu fim, 
2 - a menos que a string já termine com 'ing', nesse caso adicione 'ly'.
3 - Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""

def verbing(s):
    # +++ SUA SOLUÇÃO +++
    entrada = s
    
    if len(entrada) < 3:
        return entrada
    else:
        if entrada[-3] == 'i' and entrada[-2] == 'n' and entrada[-1] == 'g':
            return entrada+'ly'
        else:
            return entrada+'ing'


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(verbing, 'hail', 'hailing')
    test(verbing, 'log', 'loging')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
