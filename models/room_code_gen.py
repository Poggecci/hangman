def room_code_generator():
    code_as_list = ['A', 'A', 'A', 'A']
    chars = 'ABCDEFGHIJKLMNOPQRZTUVWXYZ'
    for ch0 in chars:
        code_as_list[0] = ch0
        for ch1 in chars:
            code_as_list[1] = ch1
            for ch2 in chars:
                code_as_list[2] = ch2
                for ch3 in chars:
                    code_as_list[3] = ch3
                    yield "".join(code_as_list)