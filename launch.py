#Custom libs
from data.monde import *
# from data.aspirateur import Aspirateur

if __name__ == "__main__":

  a = AspiVoyant()
  m = Monde(a,1,2)
  m.simulation(4)

  # print(m.table)
  # print(m.posAgent)
  # a.setReward(42)
  # print(a.getEvaluation())

  
