#########################################Definitions#############################################
#Manholes with attributes of size, name and depths
class Structure:
    
    def __init__(self, name, size, depth):
        self.name = name
        self.size = size
        self.depth = depth
    
    def is_receptor(self):
        if self.size == "76X37" or self.size == "37X76":
            return True
        return False


def dimenstion(df,row):
    #Cleans size text
    dim = df.loc[row, "SIZE"]        
    if "???X???" in dim:
       return df.loc[row, "SIZE"].split('D-')[1] #Returns the diameter from list of splited string
    else:
       return re.split("-| or", df.loc[row, "SIZE"])[1] #Returns rectangular dimensions list of splited string

def transpose_size(df,row):
    # prevents sizes of 120X140 and 140X120 to count as 2 diffrent sizes 
    size = df.loc[row,"SIZE"]
    if 'X' in size and size != '???X???':
        sp = size.split('X')
        return str(min(sp)) + 'X' + str(max(sp))
    else:
        return size


def convert_to_object_list(df,row):
        name = df.loc[row, "Name"]
        size = df.loc[row, "SIZE"]
        depth = df.loc[row, "DEPTH"]
        return (name, size, depth)



#adds to a list of structures 
def depth_counter(lst):
    pass

#Object list to dictionary of one of the attributes as unique keys and an empty list as value
def ol2dl(lst, att):
    a_set = set([getattr(obj, att) for obj in lst if '???' not in getattr(obj, att)])
    return dict((key, []) for key in a_set)
    

###################################################Main Code############################################################
if __name__ == "__main__":
    import pandas as pd
    import re
    from tkinter.filedialog import askopenfilename
    from tkinter import filedialog
    import numpy as np

    filename = askopenfilename(title = "Select File", filetypes = (('CSV files', '*.csv'),))

    df = pd.read_csv(filename)
    df_mh = df
    df_mh.columns = df_mh.iloc[0]           ##Makes the second row the header
    df_mh = df_mh.drop(0)
    df_mh = df_mh.drop("Details",1) 
    df_mh = df_mh.where(df_mh != '???' , 0)  ##replaces '???' from the depths with 0


    for row in range(1,len(df_mh)+1):
        df_mh.loc[row, "SIZE"] = dimenstion(df_mh,row)
        df_mh.loc[row, "SIZE"] = transpose_size(df_mh,row)


    df = df_mh


    # Structure quantification
    s_list = []

    for row in range(1,len(df)+1):
        name,size,depth = convert_to_object_list(df,row)
        s_list.append(Structure(name,size,float(depth)))


    qs = ol2dl(s_list, 'size') 
    # ^#qs for quantities structure
    # Creates a dictionary with keys of sizes and values as as an empty list of counters where:
    # index 0 is depth 0-2
    # index 1 is depth 2-3
    # index 2 is depth 3-4
    # etc.

    for key in qs:
        # First we check in range of 0-2
        counter = 0
        for obj in s_list:
                if (obj.size == key) and (obj.depth > 0 and obj.depth <= 1.25):
                    counter += 1
        qs[key].append(counter)
        # Then we check in range of 2-8 with increment of 0.5.
        for d in np.arange(1.25,7.75,0.5):
            counter = 0
            for obj in s_list:
                if (obj.size == key) and (obj.depth > d and obj.depth <= d+0.5):
                    counter += 1
            qs[key].append(counter)


    rowindex = ['0-1.25','1.25-1.75','1.75-2.25','2.25-2.75','2.75-3.25',
                '3.25-3.75','3.75-4.25','4.25-4.75','4.75-5.25','5.25-5.75',
                '5.75-6.25','6.25-6.75','6.75-7.25','7.25-7.75']

    df_new = pd.DataFrame(data=qs,
                            index=rowindex)

   

    with pd.ExcelWriter(filename.split('.csv')[0] + '-output.xlsx') as writer:
        df.to_excel(writer, sheet_name="מקור")
        df_new.to_excel(writer, sheet_name="כמויות")


    print('File exported Succesfuly')
            





