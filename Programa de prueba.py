from Ejercicio6 import ViajeroFrecuente

def mayorCantidadDeMillas (listaViajeros, i):
    viajCMayCantMillas = listaViajeros[0]
    for j in range (i):
        if listaViajeros[j] > viajCMayCantMillas:
            viajCMayCantMillas = listaViajeros[j]
    print ('El viajero con mayor cantidad de millas acumuladas es:', viajCMayCantMillas.getNombre ())

if __name__ == '__main__':
    listaViajeros = []
    i = 0
    with open ('Viajeros frecuentes.csv', '+r') as archivo:
        for linea in archivo:
            p, a, r, t, e = linea.split (',')
            listaViajeros.append (ViajeroFrecuente (p, a, r, t, e))
            i+=1
    mayorCantidadDeMillas (listaViajeros, i)
    listaViajeros[2].mostrar ()
    v = listaViajeros[2] + 100
    v.mostrar ()
    listaViajeros[0].mostrar ()
    v = listaViajeros[0] - 100
    v.mostrar ()