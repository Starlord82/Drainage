#Quantity calculation from pipe csv exported from Civil3D
#Author: Zvika Dov

#The program takes a Pipe.csv file as an input, and returns an Excel file as an output
# which organizes the data and sorts the quantities by diameter, depth and length.


import pandas as pd
from tkinter.filedialog import askopenfilename
import numpy as np

#Pipes
dia_list = [40,50,60,80,100,125,150,180,200,240,320]
widths = {40:7.5,50:8.5,60:10,80:12.4,100:14.8,125:17.5,150:18,180:20,200:20,24:240,320:30}
class Pipe():
    """docstring for ClassName"""
    
    def __init__(self, name, diameter, length):
        self.name = name      
        self.diameter = diameter
        self.length = length
        self.twidth = widths[int(self.diameter)]
        self.depth = None

    def __repr__(self):
        return self.name
        

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

def show_only_max_cover(df,row):
    '''returns depth based on max cover'''
    max_cover = float(df.loc[row,"COVER"].split('max-')[1])
    return max_cover

def ol2dl(lst, att):
    a_set = set([getattr(obj, att) for obj in lst])
    return dict((key, []) for key in a_set)


filename = askopenfilename()
df = pd.read_csv(filename)
df = delete_level(df)
df['Diameter'] = df['Diameter'].str.replace('cm','')
df['Diameter'] = pd.to_numeric(df['Diameter'])
df['Length'] = pd.to_numeric(df['Length'])
df_ex = df[['Pipe Name', 'Diameter' , 'Length']]
df_ex['Depth'] = np.nan
pipelst = []

for row in range(len(df)):
    df.loc[row,'COVER'] = show_only_max_cover(df, row)
    name = df.loc[row,'Pipe Name']
    dia = df.loc[row,'Diameter']
    length = df.loc[row,'Length']
    pipelst.append(Pipe(name,dia,length))
    pipelst[row].depth = float(df.loc[row,'COVER']) + ((float(pipelst[row].diameter))/100) + 2*(float(pipelst[row].twidth)/100)
    df_ex.loc[row,'Depth'] = pipelst[row].depth 

qp = ol2dl(pipelst, 'diameter')

for dia in qp:
    for d in range(1,8):
        total = 0
        for pipe in pipelst:
            counter = 0
            if d == 1:
                if pipe.depth <= 2 and pipe.diameter == dia:
                    total +=  float("{:.2f}".format(pipe.length))
                    
            elif (pipe.depth > d and pipe.depth <= d+1) and (pipe.diameter == dia):
                total += float("{:.2f}".format(pipe.length))  
            

            
       
        qp[dia].append(total)


row_index = ["0-2","2-3","3-4","4-5","5-6","6-7","7-8"]
df_ex_sheet_2 = pd.DataFrame(data = qp, index = row_index)
df_ex_sheet_2 = df_ex_sheet_2.reindex(sorted(df_ex_sheet_2.columns), axis = 1)
with pd.ExcelWriter(filename.split('.csv')[0] + '-output.xlsx') as writer:
        df_ex.to_excel(writer, sheet_name="מקור")
        df_ex_sheet_2.to_excel(writer, sheet_name="כמויות")

print("All Done!")







