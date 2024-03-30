
'''#IMPRESSÃO
    print("Hello Word")
        print('idade: {}  altura: {}'.format(entrada,entrada2))
        print(f"idade: {entrada} alt: {entrada2}")
        #type mostra o tipo da variável
        print(type(2))
    
    OPERERADORES ARITIMETICOS
        Os	principais	operadores	são:
            Operação Nome Descrição
            a	+	b adição Soma	entre	a	e	b
            a	-	b subtração Diferença	entre	a	e	b
            a	*	b multiplicação Produto	entre	a	e	b
            a	/	b divisão Divisão	entre	a	e	b
            a	//	b divisão	inteira Divisão	inteira	entre	a	e	b
            a	%	b módulo Resto	da	divisão	entre	a	e	b
            a	**	b exponenciação a	elevado	a	potência	de	b

    STRINGS

        O	operador    +   funciona concatenando strings,	ou	seja,	juntando	duas	strings:
                    >>>	texto1	=	'oi'
                    >>>	texto2	=	'Python'
                    texto1	+	texto2
                    oiPython
        O	operador	*	também	 funciona	com	strings,	multiplicando	 seu	 conteúdo	 por	 um	inteiro.	 Vamos
                    >>>	texto1	=	'python	'
                    >>>	texto1	*	3
                    python	python	python

        Métodos 
                    Aqui estão todos os métodos disponíveis para strings em Python, juntamente com exemplos:

                    1. **capitalize()**: Retorna uma cópia da string com o primeiro caractere em maiúsculo e o restante em minúsculo.

                    ```python
                    s = "exemplo de string"
                    print(s.capitalize())  # Saída: "Exemplo de string"
                    ```

                    2. **casefold()**: Retorna uma versão em minúsculas da string, apropriada para comparação de strings não diferenciais.

                    ```python
                    s = "Exemplo de String"
                    print(s.casefold())  # Saída: "exemplo de string"
                    ```

                    3. **center(width, fillchar)**: Retorna uma string centralizada em um campo de largura especificado.

                    ```python
                    s = "Python"
                    print(s.center(10, '*'))  # Saída: "**Python**"
                    ```

                    4. **count(substring, start, end)**: Retorna o número de ocorrências de uma substring na string.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.count("exemplo"))  # Saída: 2
                    ```

                    5. **encode(encoding="utf-8", errors="strict")**: Retorna uma versão codificada da string como uma sequência de bytes.

                    ```python
                    s = "exemplo de string"
                    print(s.encode())  # Saída: b'exemplo de string'
                    ```

                    6. **endswith(suffix, start, end)**: Verifica se a string termina com o sufixo especificado.

                    ```python
                    s = "exemplo de string"
                    print(s.endswith("string"))  # Saída: True
                    ```

                    7. **expandtabs(tabsize=8)**: Expande os caracteres de tabulação para espaços.

                    ```python
                    s = "exemplo\tde\tstring"
                    print(s.expandtabs())  # Saída: "exemplo    de      string"
                    ```

                    8. **find(substring, start, end)**: Retorna o índice da primeira ocorrência de uma substring na string. Retorna -1 se não encontrar.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.find("de"))  # Saída: 8
                    ```

                    9. **format(*args, **kwargs)**: Formata a string usando argumentos posicionais e nomeados.

                    ```python
                    name = "João"
                    age = 30
                    print("Meu nome é {} e tenho {} anos.".format(name, age))
                    # Saída: "Meu nome é João e tenho 30 anos."
                    ```

                    10. **format_map(mapping)**: Formata a string usando um mapeamento de chaves para valores.

                    ```python
                    mapping = {'name': 'João', 'age': 30}
                    print("Meu nome é {name} e tenho {age} anos.".format_map(mapping))
                    # Saída: "Meu nome é João e tenho 30 anos."
                    ```

                    11. **index(substring, start, end)**: Retorna o índice da primeira ocorrência de uma substring na string. Gera um erro se não encontrar.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.index("de"))  # Saída: 8
                    ```

                    12. **isalnum()**: Retorna True se todos os caracteres na string são alfanuméricos.

                    ```python
                    s = "abc123"
                    print(s.isalnum())  # Saída: True
                    ```

                    13. **isalpha()**: Retorna True se todos os caracteres na string são alfabéticos.

                    ```python
                    s = "abc"
                    print(s.isalpha())  # Saída: True
                    ```

                    14. **isascii()**: Retorna True se todos os caracteres na string são ASCII.

                    ```python
                    s = "abc123"
                    print(s.isascii())  # Saída: True
                    ```

                    15. **isdecimal()**: Retorna True se todos os caracteres na string são decimais.

                    ```python
                    s = "123"
                    print(s.isdecimal())  # Saída: True
                    ```

                    16. **isdigit()**: Retorna True se todos os caracteres na string são dígitos.

                    ```python
                    s = "123"
                    print(s.isdigit())  # Saída: True
                    ```

                    17. **isidentifier()**: Retorna True se a string for um identificador válido (por exemplo, um nome de variável).

                    ```python
                    s = "nome_variavel"
                    print(s.isidentifier())  # Saída: True
                    ```

                    18. **islower()**: Retorna True se todos os caracteres na string estiverem em minúsculas.

                    ```python
                    s = "exemplo"
                    print(s.islower())  # Saída: True
                    ```

                    19. **isnumeric()**: Retorna True se todos os caracteres na string forem numéricos.

                    ```python
                    s = "123"
                    print(s.isnumeric())  # Saída: True
                    ```

                    20. **isprintable()**: Retorna True se todos os caracteres na string forem imprimíveis ou a string estiver vazia.

                    ```python
                    s = "abc123"
                    print(s.isprintable())  # Saída: True
                    ```

                    21. **isspace()**: Retorna True se todos os caracteres na string forem espaços em branco.

                    ```python
                    s = "   "
                    print(s.isspace())  # Saída: True
                    ```

                    22. **istitle()**: Retorna True se a string for uma "string de título" (cada palavra começa com maiúscula).

                    ```python
                    s = "Exemplo De String"
                    print(s.istitle())  # Saída: True
                    ```

                    23. **isupper()**: Retorna True se todos os caracteres na string estiverem em maiúsculas.

                    ```python
                    s = "EXEMPLO"
                    print(s.isupper())  # Saída: True
                    ```

                    24. **join(iterable)**: Concatena elementos de um iterable (como uma lista) em uma única string, usando a string como separador.

                    ```python
                    s = "-"
                    seq = ("a", "b", "c")
                    print(s.join(seq))  # Saída: "a-b-c"
                    ```

                    25. **ljust(width, fillchar)**: Retorna uma string justificada à esquerda em um campo de largura especificado.

                    ```python
                    s = "Python"
                    print(s.ljust(10, '*'))  # Saída: "Python****"
                    ```

                    26. **lower()**: Retorna uma cópia da string com todos os caracteres em minúsculo.

                    ```python
                    s = "Exemplo de String"
                    print(s.lower())  # Saída: "exemplo de string"
                    ```

                    27. **lstrip(chars)**: Remove espaços em branco ou caracteres especificados do início da string.

                    ```python
                    s = "   exemplo de string   "
                    print(s.lstrip())  # Saída: "exemplo de string   "
                    ```

                    28. **maketrans(x, y, z)**: Retorna uma tabela de tradução usada na função translate().

                    ```python
                    x = "aeiou"
                    y = "12345"
                    z = " "
                    trans

                    _table = str.maketrans(x, y, z)
                    print(trans_table)  # Saída: {97: 49, 101: 50, 105: 51, 111: 52, 117: 53, 32: None}
                    ```

                    29. **partition(separator)**: Retorna uma tupla contendo a parte antes do separador, o próprio separador e a parte após o separador.

                    ```python
                    s = "exemplo-de-string"
                    print(s.partition("-"))  # Saída: ('exemplo', '-', 'de-string')
                    ```

                    30. **replace(old, new, count)**: Substitui todas as ocorrências de uma substring por outra.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.replace("exemplo", "teste"))  # Saída: "teste de string com teste"
                    ```

                    31. **rfind(substring, start, end)**: Retorna o índice da última ocorrência de uma substring na string. Retorna -1 se não encontrar.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.rfind("exemplo"))  # Saída: 21
                    ```

                    32. **rindex(substring, start, end)**: Retorna o índice da última ocorrência de uma substring na string. Gera um erro se não encontrar.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.rindex("exemplo"))  # Saída: 21
                    ```

                    33. **rjust(width, fillchar)**: Retorna uma string justificada à direita em um campo de largura especificado.

                    ```python
                    s = "Python"
                    print(s.rjust(10, '*'))  # Saída: "****Python"
                    ```

                    34. **rpartition(separator)**: Retorna uma tupla contendo a parte antes do separador, o próprio separador e a parte após o separador, começando pela direita.

                    ```python
                    s = "exemplo-de-string"
                    print(s.rpartition("-"))  # Saída: ('exemplo-de', '-', 'string')
                    ```

                    35. **rsplit(separator, maxsplit)**: Divide a string em substrings usando o separador especificado, começando pela direita.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.rsplit(" ", 2))  # Saída: ['exemplo de string', 'com', 'exemplo']
                    ```

                    36. **rstrip(chars)**: Remove espaços em branco ou caracteres especificados do final da string.

                    ```python
                    s = "   exemplo de string   "
                    print(s.rstrip())  # Saída: "   exemplo de string"
                    ```

                    37. **split(separator, maxsplit)**: Divide a string em substrings usando o separador especificado.

                    ```python
                    s = "exemplo de string com exemplo"
                    print(s.split())  # Saída: ['exemplo', 'de', 'string', 'com', 'exemplo']
                    ```

                    38. **splitlines(keepends)**: Divide a string em linhas. Opcionalmente, mantém os caracteres de quebra de linha.

                    ```python
                    s = "linha 1\nlinha 2\nlinha 3"
                    print(s.splitlines())  # Saída: ['linha 1', 'linha 2', 'linha 3']
                    ```

                    39. **startswith(prefix, start, end)**: Verifica se a string começa com o prefixo especificado.

                    ```python
                    s = "exemplo de string"
                    print(s.startswith("ex"))  # Saída: True
                    ```

                    40. **strip(chars)**: Remove espaços em branco ou caracteres especificados do início e do final da string.

                    ```python
                    s = "   exemplo de string   "
                    print(s.strip())  # Saída: "exemplo de string"
                    ```

                    41. **swapcase()**: Retorna uma cópia da string com a troca de maiúsculas por minúsculas e vice-versa.

                    ```python
                    s = "Exemplo de String"
                    print(s.swapcase())  # Saída: "eXEMPLO DE sTRING"
                    ```

                    42. **title()**: Retorna uma cópia da string com a primeira letra de cada palavra em maiúscula.

                    ```python
                    s = "exemplo de string"
                    print(s.title())  # Saída: "Exemplo De String"
                    ```

                    43. **translate(table)**: Retorna uma cópia da string onde cada caractere foi mapeado através da tabela de tradução fornecida.

                    ```python
                    s = "exemplo de string"
                    translation_table = str.maketrans("aeiou", "12345")
                    print(s.translate(translation_table))  # Saída: "3x4mpl4 d2 str3ng"
                    ```

                    44. **upper()**: Retorna uma cópia da string com todos os caracteres em maiúsculo.

                    ```python
                    s = "exemplo de string"
                    print(s.upper())  # Saída: "EXEMPLO DE STRING"
                    ```

                    45. **zfill(width)**: Retorna uma cópia da string preenchida com zeros à esquerda para atingir a largura especificada.

                    ```python
                    s = "42"
                    print(s.zfill(5))  # Saída: "00042"
                    ```

        OPERADORES 
            LÓGICOS(COMPARAÇÃO)
              
                    a	==	b a	igual	a	b
                    a	!=	b a	diferente	de	b
                    a	<	b a	menor	do	que	b
                    a	>	b a	maior	do	que	b
                    a	<=	b a	menor	ou	igual	a	b
                    a	>=	b a	maior	ou	igual	a	b
            BOOLEANOS
                    Outros	operadores	que	retornam	valores	booleanos	são:
                    Operação Descrição
                    a	is	b   |  True	se	a	e	b	são	idênticos
                    a	is	not	b   |   True	se	a	e	b	não	são	idênticos
                    a	in	b   |   True	se	a	é	membro	de	b
                    a	not	in	b   |   True	se	a	não	é	membro	de	b

                    É	importante	 saber	 que	 os	 operadores		==		e		is		 funcionam	 de	maneira	 diferente.	 Vamos	 usar	 o
                    exemplo	de	duas	listas	e	checar	se	elas	são	iguais:
                                    >>>	x	=	[1,	2,	3]
                                    >>>	y	=	[1,	2,	3]
                                    >>>	x	==	y
                                    True
                                    >>>	x	is	y
                                    False








        '''
