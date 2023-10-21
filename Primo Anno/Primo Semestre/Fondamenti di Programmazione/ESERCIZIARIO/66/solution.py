import albero

nove=albero.AlberoBinario(9,None,None)
otto =albero.AlberoBinario(8,None,None)
sei=albero.AlberoBinario(6,None,otto)
sette =albero.AlberoBinario(7,None,nove)
quattro=albero.AlberoBinario(4,sei,None)
cinque =albero.AlberoBinario(5,sette,None)
due =albero.AlberoBinario(2,quattro,cinque)
tre = albero.AlberoBinario(3,None,None)
uno =albero.AlberoBinario(1,due,tre)
def es66(tree):
    m, M = larghezza_albero(tree)
    return M-m


def larghezza_albero(A, pos=0):
    sx_m = sx_M = dx_m = dx_M = pos         # se non ho figli questa pos e' min e max
    if A.sx:
        sx_m, sx_M = larghezza_albero(A.sx, pos-1)
    if A.dx:
        dx_m, dx_M = larghezza_albero(A.dx, pos+1)
    return min(sx_m, dx_m), max(sx_M, dx_M)

print(es66(uno))