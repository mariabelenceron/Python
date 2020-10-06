def maskify(cc):
    # cc = str(cc)
    # cc = list(cc)
    # last_digits = []
    # first_digits = []
    # if len(cc) > 4:
    #     for i in range(4):
    #         last_digits.append(cc.pop())
    # else:
    #     cc = "".join(cc)
    #     return cc
    # if len(cc) > 4:
    #     for i in cc:
    #         first_digits.append(str(i).replace(i,'#'))
    #     resultado = first_digits + last_digits[::-1]
    #     resultado = "".join(resultado)
    #     return resultado
    return "#"*(len(cc)-4) + cc[-4:]
def run():
    print("15456454878113216878787987")
    print(maskify("15456454878113216878787987")) 

if __name__ == "__main__":
    run()   