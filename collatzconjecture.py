import time


def collatz():
    #c = float(input("Enter starting number (1 --> Any): "))
    c = 25
    collatz = []
    v=0
    kount = 0
    h1, h2, h3, h4, h5, h6, h7, h8, h9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    while c != 1 or v!=1:
        if c % 2 == 0:
            c = c / 2
            kount += 1
            c = str(c)
            if c.startswith("1"):
                h1 += 1
            elif c.startswith("2"):
                h2 += 1
            elif c.startswith("3"):
                h3 += 1
            elif c.startswith("4"):
                h4 += 1
            elif c.startswith("5"):
                h5 += 1
            elif c.startswith("6"):
                h6 += 1
            elif c.startswith("7"):
                h7 += 1
            elif c.startswith("8"):
                h8 += 1
            elif c.startswith("9"):
                h9 += 1
            c = float(c)
            collatz.append(c)
        elif c % 2 != 0:
            c = (c * 3.0) + 1.0
            kount += 1
            c = str(c)
            if c.startswith("1"):
                h1 += 1
            elif c.startswith("2"):
                h2 += 1
            elif c.startswith("3"):
                h3 += 1
            elif c.startswith("4"):
                h4 += 1
            elif c.startswith("5"):
                h5 += 1
            elif c.startswith("6"):
                h6 += 1
            elif c.startswith("7"):
                h7 += 1
            elif c.startswith("8"):
                h8 += 1
            elif c.startswith("9"):
                h9 += 1
            c = float(c)
            collatz.append(c)
            v=1
    print("THE COLLATZ CONJECTURE\n=============================\nSTEP DISPLAY\n---------------------------------\n")
    for y in collatz:
        print("(",y,")" )

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


