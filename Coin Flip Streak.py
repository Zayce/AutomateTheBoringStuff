import random

def coin_flip():
    global coin
    coin = []
    for i in range(0,100-1): # Range is 100
        if random.randint(0,1) == 0: #Heads
            coin.append("Heads")
        else: # Tails
            coin.append("Tails")
    #print(coin)
coin_flip()


def coin_streak():
    