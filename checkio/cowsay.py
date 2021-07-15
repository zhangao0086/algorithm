#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

MAXCHAR = 39

def cowsay(text):
    while '  ' in text: text = text.replace('  ', ' ')

    lines, line = [], ''
    for word in text.split(' '):
        if len(word) > MAXCHAR:
            if line:
                lines.append(line[:-1])
                line = ''
            while len(word) > MAXCHAR:
                lines.append(word[:MAXCHAR])
                word = word[MAXCHAR:]
            if word:
                line += word + ' '
        else:
            if len(line) + len(word) > MAXCHAR:
                lines.append(line[:-1])
                line = ''
            line += word + ' '
    if line: lines.append(line[:-1])
    
    max_row_len = max([len(line) for line in lines])
    if len(lines) == 1:
        content = f"< {lines[0]} >"
    else:
        content = "\n".join([f"| {lines[i]:<{max_row_len}} |" for i in range(1, len(lines) - 1)])
        if content: content += '\n'
        content = f"""/ {lines[0]:<{max_row_len}} \\
{content}\\ {lines[-1]:<{max_row_len}} /"""
    
    ans = f"""
 _{'_' * max_row_len}_
{content}
 -{'-' * max_row_len}-{COW}"""
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines

    cowsay('loooooooooooooooooooooooooooooooooooong')
