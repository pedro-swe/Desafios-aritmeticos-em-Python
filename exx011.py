#Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, decâmetros, hectômetros, decímetros, centímetros e milímetros.
medida = float(input("Digite uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
dam = medida / 10
hm = medida / 100
print("A medida de {}m corresponde a\n {}cm\n {}mm\n {}dm\n {}km\n {}dam\n {}hm".format(medida, cm, mm, dm, km, dam, hm))