from itertools import combinations
 
def anycomb(items):
    return ( comb
             for r in range(1, len(items)+1)
             for comb in combinations(items, r)
             )
 
def totalvalue(comb):
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)
 
items = (
    ("mapa", 9, 150), ("bússola", 13, 35), ("água", 153, 200), ("sanduíche", 50, 160),
    ("glicose", 15, 60), ("lata", 68, 45), ("banana", 27, 60), ("maçã", 39, 40),
    ("queijo", 23, 30), ("cerveja", 52, 10), ("bronzeador", 11, 70), ("câmera", 32, 30),
    ("camiseta", 24, 15), ("calças", 48, 10), ("sombrinha", 73, 40),
    ("calças impermeáveis", 42, 70), ("roupas impermeáveis", 43, 75),
    ("estojo", 22, 80), ("óculos", 7, 20), ("toalha", 18, 12),
    ("meias", 4, 50), ("livro", 30, 10),
    )
    
bagged = max( anycomb(items), key=totalvalue) 
print("Itens : \n  " +
      '\n  '.join(sorted(item for item,_,_ in bagged)))
val, wt = totalvalue(bagged)
print(f"Valor total : {val} \nPeso total : {-wt}")