import pandas as pd

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
        widths = {40:7.5,50:8.5,60:10,80:12.4,100:14.8,125:17.5,150:18,180:20,200:20,24:240,320:30}
        return widths[self.diameter]

def convert_to_object_list(df,row):
    return (df.loc[row,'Name'], df.loc[row,'Diameter'], df.loc[row,'Length'], df.loc[row,'Depth'])


#pipe1 = Pipe('p-1',90,130,2.5)
#print(pipe1.twidth())

pipes = {'Name' : ['P-1','P-2','P-3','P-4','P-5','P-6'], 'Diameter' : [40,60,80,50,90,60],
         'Length' : [20,56,54,26,65,54], 'Depth' : [1.3,1.4,1.4,2.5,3.6,4.3]}
df = pd.DataFrame(pipes)
print(df)
pipelst = []

for row in range(len(df)):
    n,d,l,de = convert_to_object_list(df, row)
    pipelst.append(Pipe(n,d,l,de))

