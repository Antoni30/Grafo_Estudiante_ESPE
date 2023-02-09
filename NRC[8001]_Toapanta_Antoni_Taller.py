def distancia(cost,graph,via,numCost):
   """
   Funcion que permite calcular la distancia de los nodos 

   Parametro
   -------------------------------------------
   Lista de elementos de los costos de las vias: cost
   Grafo: graph
   Via que analizaremos: via
   El costo de cada nodo: numCost

   Retorno
   -------------------------------------------
   Retorna la distancia del Nodo
   """
   #declaracion de la variable
   dist=0
   print(graph[via])
   #recorremos el  valor del grafo 
   for i in range(len(graph[via])):
      #buscamos grafo con el costo y sumamos  
      dist+=cost[(numCost,graph[via][i])]
   #retornamos la distancia
   return dist

def distanciasViasGrafo(graph,cost):
   """
   Funcion que permite recorrrer todo el grafo y mostrar toda 
   las distancias que puede recorrer hasta llegar al objetivo

   Parametro
   ------------------------------------------
   el grafo para recorrer: graph
   costo de cada via: cost

   Retorna
   ------------------------------------------
   No retorna ningun valor
   """
   #declaracion que cuenta la distancia
   costoD=0
   for i in range(len(graph[0])):
      #incrementa mas 1
      costoD+=1
      #buscamos la una de las vias y sus ramas
      if graph[0][i]== 'La joya':
         #seleccionamos una de  las ramas
         if graph[1][0]=='Tambillo':
            #Aumentamos el costo
            costoD+=1
            #y sumamos todos sus nodos
            costoD+=distancia(cost,graph,6,6)
            #imprimos la informacion de la via
            print("La Distancia es la via Casa-La Joya-Tambillo-Espe es {}".format(costoD))
            #regresa un valor atras
            costoD=1
         if graph[1][1]=='Terminal Guamani':
            #Camina un valor
            costoD+=1
            #seleccionamos la otra via
            if graph[2][1] =='Capuli':
               #aumento de distsancia
               costoD+=1
               #Sumamos la distancia de cada nodo
               costoD+=distancia(cost,graph,3,3)
               #imprimimos los valores de las via
               print("Distancia de la via Casa-Joya-Terminal Guamani-Capuli-Espe es {}".format(costoD))
               #Regresa un valor hacia atras
               costoD=2
            #seleccionamos la otra via
            if graph[2][0] =='Puente de Guajalo':
               #aumentamos el costo
               costoD+=1
               #sumamos todos los nodos 
               costoD+=distancia(cost,graph,4,4)
               #Imprimimos la distancia de nuestra via
               print("Distacia de la via Casa-Joya-Terminal Guamani-Puente de Guajalo-Espe es {}".format(costoD))
               #regresa al inicio 
               costoD=0
      if graph[0][i]=='Av. Simon Bolivar':
         #Suma de todos sus nodos
         costoD+= distancia(cost,graph,5,5)
         #distancia de la via
         print("Distancia de la via Casa-Av. Simon Bolivar es {}".format(costoD))
        
if __name__ == '__main__':
   # createamos el grafo
   graph, cost = [[] for i in range(7)], {}
   graph[0].append('La joya')
   graph[0].append('Av. Simon Bolivar')
   graph[1].append('Tambillo')
   graph[1].append('Terminal Guamani')
   graph[2].append('Puente de Guajalo')
   graph[2].append('Capuli')
   graph[3].append('Recreo')
   graph[3].append('Marin')
   graph[3].append('Desvio')
   graph[3].append('Universidad ESPE')
   graph[4].append('Desvio')
   graph[4].append('Universidad ESPE')
   graph[5].append('Desvio')
   graph[5].append('Universidad ESPE')
   graph[6].append('Uyumbicho')
   graph[6].append('Amaguania')
   graph[6].append('Choclo')
   graph[6].append('Colibri')
   graph[6].append('Universidad ESPE')
   #creamos los costos de cada nodo
   cost[(0,'La joya')]=1
   cost[(0,'Av. Simon Bolivar')]=1
   cost[(1,'Tambillo')]=1
   cost[(1,'Terminal Guamani')]=1
   cost[(2,'Puente de Guajalo')]=1
   cost[(2,'Capuli')]=1
   cost[(3,'Recreo')]=1
   cost[(3,'Marin')]=1
   cost[(3,'Desvio')]=1
   cost[(3,'Universidad ESPE')]=1
   cost[(4,'Desvio')]=1
   cost[(4,'Universidad ESPE')]=1
   cost[(5,'Desvio')]=1
   cost[(5,'Universidad ESPE')]=1
   cost[(6,'Uyumbicho')]=1
   cost[(6,'Amaguania')]=1
   cost[(6,'Choclo')]=1
   cost[(6,'Colibri')]=1
   cost[(6,'Universidad ESPE')]=1
   #Mostramos toda la informacio
   print("Punto inicial Casa")
   print("Punto de llegada ESPE")
   #muestra toda la infromacion de nuestro grafo con sus costos
   distanciasViasGrafo(graph,cost)
   

         