#Importacion de CSV para la lectura del archivo
import csv
#Definicion de la clase 
class lectura:
    #contructor de la clase 
    def __init__(self):
        #define las propiedades y lee el archivo CSV
        self.mat =[]
        self.vaMax=0
        self.fil=[]
        self.col=[]
        with open('archivo.csv','r') as fil:
            arch = csv.reader(fil)
            for fila in arch:
                valores = fila[0].split(";")
                valores_enteros = [int(valor) for valor in valores]
                self.mat.append(valores_enteros)
    #busca el numero mayor de la matris y se lo resta a la matris 
    def mubMax(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if (self.vaMax< self.mat[i][j]):
                    self.vaMax=self.mat[i][j]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]=self.vaMax-self.mat[i][j]
    #resta el valor menor de cada fila y le resta a la fila corespondiente  
    def resfil(self):
        
        for i in range(len(self.mat)):
            mini=self.vaMax
            for j in range(len(self.mat[0])):
                if (mini>self.mat[i][j]):
                    mini=self.mat[i][j]
            for j in range(len(self.mat[0])):
                self.mat[i][j]-=mini  
    #resta el valor menor de cada columna y le resta a la fila corespondiente   
    def rescol(self):
        
        for i in range(len(self.mat)):
            mini=self.vaMax
            for j in range(len(self.mat[0])):
                if (mini>self.mat[j][i]):
                    mini=self.mat[j][i]
            for j in range(len(self.mat[0])):
                self.mat[j][i]-=mini
    #descarta la fila y columna donde hay mas de un 0 en ello 
    def descartar(self):
        con=0
        for fila in self.mat:
            if (fila.count(0)>1):
                self.fil.append(con)
            con+=1
        
        for i in range(len(self.mat[0])):
            count=0
            con=0
            for fila in self.mat:
                if (fila[i]==0 and not(con in self.fil)):
                    count+=1
                if count>1:
                    self.col.append(i)
                con+=1
    #procedimiento si no se cumple la condicion del descarte 
    def sol(self):
        mini=10
        for i in range(len(self.mat)):
            if not(i in self.fil):
                for j in range(len(self.mat[0])):
                    if not(j in self.col):
                        if (mini>self.mat[i][j]):
                            mini=self.mat[i][j]
        for i in range(len(self.mat)):
            if not(i in self.fil):
                for j in range(len(self.mat[0])):
                    if not(j in self.col):
                        self.mat[i][j]-=mini
        for i in range(len(self.mat)):
            if (i in self.fil):
                for j in range(len(self.mat[0])):
                    if (j in self.col):
                        self.mat[i][j]+=mini
    # imprime las posible soluciones 
    def resul(self):
        for i in range(len(self.mat[0])):
            print("el profesor {0:3>} puede dar la clase".format(i+1),end=" ")
            for j in range(len(self.mat)):
                if self.mat[j][i]==0:
                      print(j+1,end=" ") 
            print()
            
    #imprime la matris             
    def fortamo(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                print(self.mat[i][j],end=" ")
            print()
        print("-------------------------")
