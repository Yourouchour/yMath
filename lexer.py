from re import findall, match

def lexer(expression):
    '''词法分析'''
    tokens = []
    pattern = r'\d+\.?\d*|[a-zA-Z&][a-zA-Z0-9_]*\(?|\(|\)|\[|\]|<->|!=|>=|<=|\+-|\^\(|_\(|[-+*/=<>,%.]'    
    for token in findall(pattern, expression):
        if match(r'\d+.?\d*', token):
            tokens.append(('MN', token))
        elif match(r'[a-zA-Z&][a-zA-Z0-9]*\(?', token):
            if token.endswith('('):
                tokens.append(('FN', token[:-1]))
            else:
                tokens.append(('MI', token))
        else:
            tokens.append(('MO', token))
    return tokens