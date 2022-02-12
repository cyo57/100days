def text_view():
    import os
    import time

    content = 'Hello, World!   '

    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code():
    import random
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(4):
        code += chars[random.randint(0, len(chars))]
    print(code)


#text_view()
generate_code()