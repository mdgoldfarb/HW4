# HW4

The evolve function looks at every square on the grid and counts how many "True" (alive) neighbors there are and makes it False if there is over/underpopulation, and True if the square is originally dead, but hhas a certain number of neighbors, or if its alive with 2-3 neighbors and it continues to live.

The conditions are done by taking the indicies and adding/subtracting one and performing a modulus on them so it can warp around and not have an index error. There are lots of if statement for if the box is true or false, and if the sums are between or are certain values, in which the box can change its color (black or white). 
The evolve function does 1 iteration, so there is a loop that recurses on that function for 100 times prints out every 10th grid.

The visualize function helps visualizes the graph by using the pyplot as plt package. 

The animate function helps create the subplots for the animation of the video of the iterations done on the grid for the "Game of Life" and shows the glider animation of how it "glides" downward and diagonal. It does in the video variable with the video function for one of the parameters, which is a list of all the outcomes when the grid is evolved. 

To run the code, if you are using an Anaconda Terminal or other terminal, just type "python" then the file name and the value for "k" (the number of iterations the grid will go through the evolve function"

There were no functions for the first part, there was just matrix operations to get a rank vector, and eigenvalues and eigenvectors of the normalized matrixm "M", just simply type "python" in the terminal and the file name and it should give a long list a vectors that eventually show a convergence, and the Eigenvector of M and the ranking vector, r after the convergence. 

The nplinalg, loop and dot product were used. 

To run the code, just go to a terminal, type "pyhton" and the file name.
