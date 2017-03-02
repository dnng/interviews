import sys
from random import randrange

prices = []

def populate(p):
    for i in range(20):
        prices.append(randrange(1,int(sys.argv[1])))
    return p

def getmaxprofit(p):
    mi, ma, ran = 0, 0, 0
    for i in range(0, len(p)):
        for j in range(i+1, len(p)):
            if (p[j] > p[i]):
                if ((p[j] - p[i]) > ran):
                    ran = p[j] - p[i]
                    ma = j
                    mi = i
    return p[mi], p[ma]

def O_n_getmaxprofit(p):
    mi, ma, ran = 0, 0, 0
    for i in range(len(p)):
        if ((i + 1) > len(p)):
            return mi, ma
        elif ((p[i+1] - p[mi]) > ran):
            ran = p[i+1] - p[mi]
            ma = i + 1
        if ((i + 1) < mi):
            mi = i + 1

if __name__ == '__main__':
    prices     = populate(prices)
    mi, ma     = getmaxprofit(prices)
    O_mi, O_ma = O_n_getmaxprofit(prices)
    print prices
    print mi, ma
    print O_mi, O_ma

