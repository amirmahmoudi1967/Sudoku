# -*- coding: utf-8 -*-
"""
@author: Amir Mahmoudi
"""


import random as rnd
from ortools.sat.python import cp_model

class sudoku:
    def __init__(self, nb):
        if nb==0:
            self.mat=[[]]
        else:
            #init a sudoku matrix
            self.mat=[[2,8,3,5,1,9,7,4,6],[9,6,4,8,7,3,5,2,1],[5,1,7,6,2,4,9,3,8],[1,5,6,7,4,2,3,8,9],[4,2,9,3,8,6,1,7,5],[3,7,8,1,9,5,2,6,4],[8,9,5,4,3,7,6,1,2],[7,4,2,9,6,1,8,5,3],[6,3,1,2,5,8,4,9,7]]
            
            for n in range (81-nb):
                i=rnd.randint(0,8)
                j=rnd.randint(0,8)
                while self.mat[i][j]==0:
                    i=rnd.randint(0,8)
                    j=rnd.randint(0,8)
                self.mat[i][j]=0 
     
    def __str__(self):
        string=""
        for i in range(9):
            for j in range(9):
                string+=str(self.mat[i][j])
                string+="  "
            string+="\n"
        return string
  


# Résolution    
    
def difficulté():
    diff=""
    temp=False
    while temp==False:
        n=int(input("Choose difficulty (17,26,33,40 ou 50 cases)"))
        if n==17:
            temp=True
            diff="Very Hard"
        if n==26:
            temp=True
            diff="Hard"
        if n==33:
            temp=True
            diff="Medium"
        if n==40:
            temp=True
            diff="Easy"
        if n==50:
            temp=True
            diff="Beginneer"     
    print ("You choosed:  ", diff)
    return n
   

nveau=sudoku(difficulté())
print(" \n\nsudoku to solve:")
print(nveau)

model = cp_model.CpModel()
solution=[[]]
for i in range(0,9):
    for j in range(0,9):
        if nveau.mat[i][j]!=0:
            solution[i].append(model.NewIntVar(int(nveau.mat[i][j]),int(nveau.mat[i][j]),'%i %i' %(i,j)))
           
        else:
            solution[i].append(model.NewIntVar(1,9,'%i %i' %(i,j)))
          
    solution.append([])
for i in range(9):
    model.AddAllDifferent([solution[i][0],solution[i][1],solution[i][2],solution[i][3],solution[i][4],solution[i][5],solution[i][6],solution[i][7],solution[i][8]])

for i in range(9):
    model.AddAllDifferent([solution[0][i],solution[1][i],solution[2][i],solution[3][i],solution[4][i],solution[5][i],solution[6][i],solution[7][i],solution[8][i]])
    
for i in range(0,9,3):
    for j in range(0,9,3):
        model.AddAllDifferent([solution[i][j],solution[i+1][j],solution[i+2][j],solution[i][j+1],solution[i+1][j+1],solution[i+2][j+1],solution[i][j+2],solution[i+1][j+2],solution[i+2][j+2]])

solver = cp_model.CpSolver()
status = solver.Solve(model)
    
if status == cp_model.FEASIBLE:
    print ('solved sudoku:')
    print("\n")
    string="" 
    for i in range(9):
        for j in range(9):
            string+=str(solver.Value(solution[i][j]))
            string+="  "
        string+="\n"
    print(string)
    
if status != cp_model.FEASIBLE:
    print("Non Resolvable")
       
  
        
        
        
        
        
        
        
        
        
