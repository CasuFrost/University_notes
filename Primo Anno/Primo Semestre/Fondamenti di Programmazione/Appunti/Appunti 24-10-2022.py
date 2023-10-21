import random

def k_massimi_da_seq_casuale(k,N,seed):
    random.seed(seed)
    massimi=[]
    for _ in range(N):
        X = random.randint(-1000000,1000000)
        aggiorna_k_massimi(massimi,X,k)
    print(massimi)
def TEST(massimi,X,k):
    massimi.append(X)
    if len(massimi)>k:
        massimi.pop(0)
def aggiorna_k_massimi(L,X,k):
    if len(L)<k:
        L.append(X)
        return
    minimo = min(L)
    if X<=minimo:
        return
    L.remove(minimo)
    L.append(X)
k_massimi_da_seq_casuale(11, 10000, 0)

def aggiorna_k_massimi_ordinati(Lordinata,X,K):
    pass
