from os import system
import sys
import re as _re

_FUNCS = {
    'msup'    : ('<msup><mrow>',            '</mrow></msup>'),
    'msub'    : ('<msub><mrow>',            '</mrow></msub>'),
    'msubsup' : ('<msubsup><mrow>',         '</mrow></msubsup>'),
    'mfrac'   : ('<mfrac><mrow>',           '</mrow></mfrac>'),
    'mroot'   : ('<mroot><mrow>',           '</mrow></mroot>'),
    'msqrt'   : ('<msqrt><mrow>',           '</mrow></msqrt>'),
    'mspace'  : ('<mspace>',                '</mspace>'),
    'log'     : ('<msub><mi>log</mi><mrow>','</mrow></msub>')
}
_IDS = {
    'PI'     : 'π',
    'INFIN'  : "∞",
    'INT'    : "∫",
    'ALPHA'  : "α",
    'BETA'   : "β",
    'GAMMA'  : "γ",
    'DELTA'  : "Δ",
    'THETA'  : "θ",
    'LAMBDA' : "λ",
}

_OPS = {
    '*'    : '×',
    '/'    : '÷',
    '+-'   : "±",
    '!='   : "≠",
    '>='   : "≥",
    '<='   : "≤",
    '<->'  : "⟺",
}


def lexer(expression):
    '''词法分析'''
    tokens = []
    pattern = r'\d+\.?\d*|[a-zA-Z&][a-zA-Z0-9_]*\(?|\(|\)|\[|\]|<->|!=|>=|<=|\+-|\^\(|_\(|[-+*/=<>,%.]'    
    for match in _re.findall(pattern, expression):
        if(_re.match(r'\d+.?\d*', match)):
            tokens.append(('MN', match))
        elif(_re.match(r'[a-zA-Z&][a-zA-Z0-9_]*\(?', match)):
            if(match.endswith('(')):
                tokens.append(('FN', match[:-1]))
            else:
                tokens.append(('MI', match))
        else:
            tokens.append(('MO', match))
    return tokens

def parse(tokens):
    '''语法分析'''
    funclayer = {}
    layer = 0
    ans = ["<math xmlns=\"http://www.w3.org/1998/Math/MathML\">"]
    for token in tokens:
        if(token[0] == 'FN'):
            layer += 1
            words = _FUNCS.get(token[1],None)
            if(words is None):
                print(f'未定义的函数`{token[1]}()`，你是想输入`{token[1]} ()`吗')
                system('pause')
                exit()
            ans.append(words[0])
            funclayer[layer] = words[1]
            
        elif(token[0] == 'MI'):
            if(token[1].startswith('&')):
                ans.append(f'<mi>{_IDS.get(token[1][1:],token[1])}</mi>')
            else:
                ans.append(f'<mi>{token[1]}</mi>')

        elif(token[0] == 'MN'):
            ans.append(f'<mn>{token[1]}</mn>')

        elif(token[0] == 'MO'):
            if(token[1] == '('):
                layer += 1
                ans.append('<mo>(</mo>')

            elif(token[1] == ')'):
                if(func:=funclayer.get(layer, False)):
                    ans.append(func)
                    funclayer.pop(layer)
                else:
                    ans.append('<mo>)</mo>')
                layer -= 1

            elif(token[1] == ','):
                if(func:=funclayer.get(layer, False)):
                    ans.append('</mrow><mrow>')
                else:
                    ans.append('<mo>,</mo>')

            elif(token[1] == '%'):
                ans.append('<mspace></mspace>')

            elif(token[1] == '^('):
                layer += 1
                ans.insert(len(ans)-1, '<msup>')
                ans.append('<mrow>')
                funclayer[layer] = '</mrow></msup>'

            elif(token[1] == '_('):
                layer += 1                
                ans.insert(len(ans)-1, '<msub>')                
                ans.append('<mrow>')                
                funclayer[layer] = '</mrow></msub>'
            
            else:
                ans.append(f'<mo>{_OPS.get(token[1],token[1])}</mo>')
    ans.append("</math>")
    for i in ans:
        print(i, end='')


def main():
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            with open(file, 'r') as f:
                for line in f:
                    parse(lexer(line))
                    print("\n")
    else:
        while True:
            try:
                parse(lexer(input(">>> ")))
                print("\n")
            except EOFError:
                break


if __name__ == '__main__':
    main()
    input()
