palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print("="*20)
    print(f"- {p}".upper())
    print(f"Vogais:", end=' ')
    for letras in p:
        if letras.upper() in 'AEIOU':
            print(f"\033[1;31m{letras.upper()}\033[m", end=' ')
    print('')
