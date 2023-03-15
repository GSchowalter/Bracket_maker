from pick import main as pick

while(True): 
    fav = input()
    under = input()
    args = {'favorite': fav, 'underdog': under}
    pick(args)
