from tkinter import *


root = Tk()
root.minsize(275,283)
root.maxsize(275,283)


class Suduku():
    

    def __init__(self):
        self.autocor()
        self.ansfun()


    # Initializing Empty Cells to 0
    def autocor(self):
        for i in range(9):
            for j in range(9):
                if matrix[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    matrix[i][j].set(0)


    # Algorithm for finding correct answer
    def ansfun(self, i=0, j=0):
        i,j = self.findNextCellToFill(i, j)

        # If i == -1 the position is Ok or the Sudoku is Solved
        if i == -1:
            return True
        for e in range(1,10):
            if self.isValid(i,j,e):
                matrix[i][j].set(e)
                if self.ansfun(i, j):
                    return True
                # Undo the current cell for backtracking
                matrix[i][j].set(0)
        return False


    # Searching the Nearest Cell to fill
    def findNextCellToFill(self, i, j):

        for x in range(i,9):
            for y in range(j,9):
                if matrix[x][y].get() == '0':
                    return x,y

        for x in range(0,9):
            for y in range(0,9):
                if matrix[x][y].get() == '0':
                    return x,y

        return -1,-1


    # Checking the Validity of matrix[i][j]
    def isValid(self, i, j, e):

        for x in range(9):
            if matrix[i][x].get() == str(e):
                return False

        for x in range(9):
            if matrix[x][j].get() == str(e):
                return False
    
        secTopX, secTopY = 3 *int((i/3)), 3 *int((j/3))
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if matrix[x][y].get() == str(e):
                    return False
        return True
        



class Launch():
    
    # Set Title, Grid and Menu
    def __init__(self, master):
        
        # Title and settings
        self.master = master
        master.title("Sudoku Solver")

        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0
        
        # Front-end Grid
        self.__table = []
        for i in range(1,10):
            self.__table += [[0,0,0,0,0,0,0,0,0]]

        for i in range(0,9):
            for j in range(0,9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'white'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'white'
                else:
                    color = 'lightgray'

                self.__table[i][j] = Entry(master, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'orange', highlightthickness = 1.1, highlightbackground = 'black',
                                          textvar = matrix[i][j])
                self.__table[i][j].bind('<Motion>', self.correctGrid)
                self.__table[i][j].bind('<FocusIn>', self.correctGrid)
                self.__table[i][j].bind('<Button-1>', self.correctGrid)
                self.__table[i][j].grid(row=i, column=j)


        # Front-End Menu
        menu = Menu(master)
        master.config(menu = menu)

        file = Menu(menu, tearoff = 0) 
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)
        file.add_separator() 
        file.add_command(label = 'Exit', command = master.quit)

        #helpmenu = Menu(menu, tearoff=0)
        #menu.add_cascade(label="Help", menu=helpmenu)
        #helpmenu.add_command(label="About us")

    #def About(self):
        #print ("This is a simple example of a menu")
    
    # Correct the Grid if inputs are uncorrect
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if matrix[i][j].get() == '':
                    continue
                if len(matrix[i][j].get()) > 1 or matrix[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    matrix[i][j].set('')


    # Clear the Grid
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                matrix[i][j].set('')



    # Calls the class Suduku
    def solveInput(self):
        solution = Suduku()

        
        

# Global Matrix where default numbers or blank spaces are stored
matrix = []
for i in range(1,10):
    matrix += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        matrix[i][j] = StringVar(root)


app = Launch(root)
#ab=Label(root,text="By Dhruvil Vachhani",fg='#343434',font=('Arial',12))
#ab.grid(row=13,column=1,columnspan=12)
root.mainloop()