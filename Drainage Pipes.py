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
    t = (df.loc[row,' Pipe Name'], df.loc[row,'Diameter'], df.loc[row,'Length'], df.loc[row,'Depth'])
    return t

def delete_level(df_input):
    '''removes first level'''
    df_input = df_input.rename(columns = df_input.iloc[0])
    df_input = df_input.drop(0)
    df_input = df_input.reset_index(drop = True)
    return df_input

def find_depth(df,row):
    '''returns depth based on max cover'''
    max_cover = float(df.loc[row,"COVER"].split('max-')[1])
    depth = max_cover 
    return depth

def replace_depth(df,row):
    pass

def remove_cm(df):
    '''removes cm from data frame'''
    for row in range(len(df)):
        df.loc[row,'Diameter'].replace('cm','')
    return(df)




filename = askopenfilename()
df = pd.read_csv(filename)
df = delete_level(df)
print(find_depth(df,0))
df = remove_cm(df)

print(df)

# pipelst = []
# for row in range(len(df)):
#     n,d,l,de = convert_to_object_list(df, row)
#     pipelst.append(Pipe(n,d,l,de))

# for pipe in pipelst:
#     print(pipe.name,pipe.diameter,pipe.twidth())

