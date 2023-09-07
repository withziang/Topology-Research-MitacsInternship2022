#                            Honours Research--Topology   
#                                    Ziang Wang
#          Code is for find the dimension of homology of graph (R^2) (Betti Number)

"""Use .txt file for input, enumerate simplices, every simplex occupy a line. 
                            Edge needs to be in order!!!
                        Cannot have more than 10 vertix or edge

               e.g
                   {1,2,3,4,5,6} for 1-dimensional and {12,23,45} for 2-dimensional 
        write:
                                 ////    1
                                         2
                                         3
                                         4
                                         5
                                         6
                                         12
                                         23
                                         45                  ////

                         in the txt file
"""
#create an object for the graph 
class Graph: 
     def __init__(self, Input_data):
         self.Input_data = Input_data
         #seperate the simplex array in to Edge and Vertix subarray
         self.Edge_data = []
         self.Vertix_data = []
         for element in self.Input_data:
             if element < 10:
                 self.Vertix_data.append(element)                    #array
             if element >= 10:
                 self.Edge_data.append(element)                      #array
     #functions get the result
     def get_Edge_data(self):
         return self.Edge_data 
     def get_Vertix_data(self):
         return self.Vertix_data

  
#function to put graph into a matrix
def Rank_of_the_graph(Edge_array, Vertix_array):
     import numpy as np
     Matrix = np.zeros([len(Vertix_array),len(Edge_array)], dtype = int)
     i = 0
     for element in Edge_array:
         Matrix[int(element) % 10 -1][i] = 1                    # boundry operator: ones digit minus tens digit
         Matrix[int(element) //10 -1][i] = -1
         i += 1
     return np.linalg.matrix_rank(Matrix)                       # rank is for d1

#homology function 
"""     H0 = ker(d0) / Im(d1), dim(H0) = dim(d0)-rank(d1)       """
def get_the_dimension_of_H0(Vertix_array, rank):
     return len(Vertix_array) - rank

"""     H1 = ker(d1) / Im(d2), dim(H1) = (number of Edge - rank(d1)) - 0  """
def get_the_dimension_of_H1(Edge_array, rank):
     return len(Edge_array) - rank





#Read the file, possible improvement: analysis several files at the same time
txtfile_path = input("Input txt file path please:\n")
file = open(txtfile_path,"r")                          # an object
Input_value = []
for number in file:
    Input_value.append(int(number))                    #array
file.close()

#add multiple graphes if there are many files
Graph1 = Graph(Input_value)
rank1 = Rank_of_the_graph(Graph1.get_Edge_data(), Graph1.get_Vertix_data())


#final output
print("dim of H0 is", get_the_dimension_of_H0(Graph1.get_Vertix_data(), rank1))
print("dim of H1 is", get_the_dimension_of_H1(Graph1.get_Edge_data(), rank1))


