import matplotlib.pyplot as plt
import numpy as np

#O ficheiro tem 2 linhas. A primeira linha s�o os golos da HomeTeam e a segunda os golos a AwayTeam.
#Cada linha acaba com space + \n logo tenho de fazer o strip() deles
with open("Goals.txt","r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]  
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

#Se n�o defenirmos a colunaX � criada por default. Ver documenta��o "import matplotlib.pyplot as plt \n help(plt.pyplot)"
plt.plot(HomeTeamGoals)
plt.plot(AwayTeamGoals)
plt.show()

#Demostra��o para a ausencia do X na fun��o plot()
#Calcula numero de elementos do array
xVariable = np.arange(len(HomeTeamGoals))
plt.plot(xVariable, AwayTeamGoals)
plt.show()
plt.plot(xVariable, HomeTeamGoals)
plt.show()


#Scatter() representa apenas os pontos do gr�fico
plt.scatter(xVariable, AwayTeamGoals, c = "green", s = 12)
plt.show()
plt.scatter(xVariable, HomeTeamGoals, c = "red", s = 12)
plt.xlim(0,145) #Mudar o limite do vetorX. xlim(lower,upper)
plt.ylim(-0.5,6) #Mudar o limite do vetorY. ylim(lower,upper)
plt.show()