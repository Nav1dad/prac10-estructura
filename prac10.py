# PANDAAS Y MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt

fbk = ["Facebook", 2449, 2006]
twt = ["Twitter", 339, 2006]
ig = ["Instagram", 1000, 2009]
yt = ["YouTube", 2000, 2005]
wsp = ["Whatsapp", 1600, 2009]

lista_redes = [fbk, twt, ig, yt, wsp]

df_redes = pd.DataFrame(lista_redes, columns=['nombre', 'cantidad', 'año'])

plt.plot(df_redes["nombre"], df_redes["cantidad"])
plt.title("Diagrama de lineas")
plt.xlabel("Redes")
plt.ylabel("Cantidad")
plt.show()