#Quantity calculation from pipe csv exported from Civil3D
#Author: Zvika Dov

#The program takes a Pipe.csv file as an input, and returns an Excel file as an output
# which organizes the data and sorts the quantities by diameter, depth and length.


import pandas as pd
from tkinter.filedialog import askopenfilename

#Pipes
class Pipe():
    """docstring for ClassName"""
    dia_list = [40,50,60,80,100,125,150,180,200,240,320]
    def __init__(self, name, diameter, length, maxdepth):
        self.name = name
        self.diameter = diameter
        while True:
            try:
                if self.diameter in [40,50,60,80,100,125,150,180,200,240,320]:
                    break
                else:
                    self.diameter = int(input(self.name + ' has a bad diameter value\nPlease choose a new diameter from the list:\n''40,50,60,80,100,125,150,180,200,240,320\n'))
            except:
                print('Please enter a whole number!')
        self.length = length
        self.maxdepth = maxdepth

    def twidth(self):
        '''returns flange width by diameter'''
        widths = {40:7.5,50:8.5,60:10,80:12.4,100:14.8,125:17.5,150:18,180:20,200:20,24:240,320:30}
        return widths[self.diameter]

def convert_to_object_list(df,row):
    '''returns tuples of values from dataframe'''
    return (df.loc[row,'Name'], df.loc[row,'Diameter'], df.loc[row,'Length'], df.loc[row,'Depth'])

def delete_level(df):
    '''removes first level'''
    df.columns = df.iloc[0]
    df = df.drop(0)
    return df



filename = askopenfilename()
df = pd.read_csv(filename)
# df = delete_level(df)
#I NEED TO REPLACE THE HEADING WITH DF.RENAME()
print(df)



# for row in range(len(df)):
#     n,d,l,de = convert_to_object_list(df, row)
#     pipelst.append(Pipe(n,d,l,de))

# for pipe in pipelst:
#     print(pipe.name,pipe.diameter,pipe.twidth())

