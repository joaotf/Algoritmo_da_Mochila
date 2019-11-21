def Algoritmo_Mochila(W,wt,val,n): 
    if n == 0 or W == 0 : 
        return 0

    if (wt[n-1] > W): 
        print(f"W ==> {W}")
        return Algoritmo_Mochila(W , wt , val , n-1) 
    else: 
        print(f"W ==> {W}")
        return max(val[n-1] + Algoritmo_Mochila(W-wt[n-1] , wt , val , n-1), 
                   Algoritmo_Mochila(W , wt , val , n-1)) 
  

val = [60, 100, 120, 200] # Valor
wt = [10, 20, 30 , 50] # Peso
W = 200 # Capacidade da mochila
n = len(val) 

print("Solução ==> ",Algoritmo_Mochila(W , wt , val , n))