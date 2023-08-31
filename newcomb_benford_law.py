import time
#helo hi helelo
def digit_calc(numstr,countlist):
    for i in range(1,10):
    if numstr.startswith(str(i)):
        for j in countlist:
            if str(i) in j:
                j += 1
    return countlist


def collatz():
    c = float(input("Enter starting number (1 --> Any): "))
    collatz = []
    v=0
    kount = 0
    h1, h2, h3, h4, h5, h6, h7, h8, h9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    hlst = [h1, h2, h3, h4, h5, h6, h7, h8, h9]
    while c != 1 or v!=1:
        if c % 2 == 0:
            c = c / 2
            kount += 1
            c = str(c)
            hlist = digit_calc(c,hlist)

        elif c % 2 != 0:
            c = (c * 3.0) + 1.0
            kount += 1
            c = str(c)
            hlist = digit_calc(c,hlist)
        c = float(c)
        collatz.append(c)

    print("\nSteps: ",kount,"\n---------------------------------")
    histotrac = dict(zip((1, 2, 3, 4, 5, 6, 7, 8, 9), (h1, h2, h3, h4, h5, h6, h7, h8, h9)))
    
    print("GRAPHICAL DISPLAY\n---------------------------------\nkey: up to down --> 1-9")
    for k in histotrac.keys():
        for u in range(histotrac[k]):
            print("▩", end='')
        print(k, ": (", (histotrac[k] / sum(histotrac.values())) * 100, "% )")

    print("BENFORD'S LAW displayed: https://cutt.ly/vO7ninN ")
    print("---------------------------------")
    
    print("Stats: ", histotrac)

collatz()
