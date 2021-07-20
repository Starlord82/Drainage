#Definitions
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
#Pipes
class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
#Cleans size text
def dimenstion(df,row):

    dim = df.loc[row, "SIZE"]        
    if "???X???" in dim:
       return df.loc[row, "SIZE"].split('D-')[1] #Returns the diameter from list of splited string
    else:
       return re.split("-| or", df.loc[row, "SIZE"])[1] #Returns rectangular dimensions list of splited string


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
    filename = askopenfilename()

    df = pd.read_csv(filename)
    df_mh = df
    df_mh.columns = df_mh.iloc[0]
    df_mh = df_mh.drop(0)
    df_mh = df_mh.drop("Details",1)
    df_mh = df_mh.where(df_mh != '???' , 0)  ##replaces '???' from the depths witn 0


    for row in range(1,len(df_mh)+1):
        df_mh.loc[row, "SIZE"] = dimenstion(df_mh,row)

    df = df_mh


    #Structure quantification
    s_list = []

    for row in range(1,len(df)+1):
        name,size,depth = convert_to_object_list(df,row)
        s_list.append(Structure(name,size,float(depth)))


    qs = ol2dl(s_list, 'size')
    #^#
    #Creates a dictionary with keys of sizes and values as list counters where
    #index 0 is depth 0-2
    #index 1 is depth 2-3
    #index 2 is depth 3-4
    #etc.


    

    # ##Counting of structurs###
    # s_100x120_0_2 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 0  and x.depth<=2]
    # s_100x120_2_3 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 2  and x.depth<=3]
    # s_100x120_3_4 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 3  and x.depth<=4]
    # s_100x120_4_5 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 4  and x.depth<=5]
    # s_100x120_5_6 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 5  and x.depth<=6]
    # s_100x120_6_7 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 6  and x.depth<=7]
    # s_100x120_7_8 = [x for x in s_list if (x.size == "100X120" or x.size == "120X100") and x.depth > 7  and x.depth<=8]

    # s_100x100_0_2 = [x for x in s_list if (x.size == "100X100") and x.depth > 0  and x.depth<=2]
    # s_100x100_2_3 = [x for x in s_list if (x.size == "100X100") and x.depth > 2  and x.depth<=3]
    # s_100x100_3_4 = [x for x in s_list if (x.size == "100X100") and x.depth > 3  and x.depth<=4]
    # s_100x100_4_5 = [x for x in s_list if (x.size == "100X100") and x.depth > 4  and x.depth<=5]
    # s_100x100_5_6 = [x for x in s_list if (x.size == "100X100") and x.depth > 5  and x.depth<=6]
    # s_100x100_6_7 = [x for x in s_list if (x.size == "100X100") and x.depth > 6  and x.depth<=7]
    # s_100x100_7_8 = [x for x in s_list if (x.size == "100X100") and x.depth > 7  and x.depth<=8]

    # s_80_100_0_2 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 0  and x.depth<=2]
    # s_80_100_2_3 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 2  and x.depth<=3]
    # s_80_100_3_4 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 3  and x.depth<=4]
    # s_80_100_4_5 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 4  and x.depth<=5]
    # s_80_100_5_6 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 5  and x.depth<=6]
    # s_80_100_6_7 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 6  and x.depth<=7]
    # s_80_100_7_8 = [x for x in s_list if (x.size == "80X100" or x.size == "100X80") and x.depth > 7  and x.depth<=8]

    # s_120x140_0_2 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 0  and x.depth<=2]
    # s_120x140_2_3 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 2  and x.depth<=3]
    # s_120x140_3_4 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 3  and x.depth<=4]
    # s_120x140_4_5 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 4  and x.depth<=5]
    # s_120x140_5_6 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 5  and x.depth<=6]
    # s_120x140_6_7 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 6  and x.depth<=7]
    # s_120x140_7_8 = [x for x in s_list if (x.size == "120X140" or x.size == "140X120") and x.depth > 7  and x.depth<=8]

    # s_150x150_0_2 = [x for x in s_list if (x.size == "150X150") and x.depth > 0  and x.depth<=2]
    # s_150x150_2_3 = [x for x in s_list if (x.size == "150X150") and x.depth > 2  and x.depth<=3]
    # s_150x150_3_4 = [x for x in s_list if (x.size == "150X150") and x.depth > 3  and x.depth<=4]
    # s_150x150_4_5 = [x for x in s_list if (x.size == "150X150") and x.depth > 4  and x.depth<=5]
    # s_150x150_5_6 = [x for x in s_list if (x.size == "150X150") and x.depth > 5  and x.depth<=6]
    # s_150x150_6_7 = [x for x in s_list if (x.size == "150X150") and x.depth > 6  and x.depth<=7]
    # s_150x150_7_8 = [x for x in s_list if (x.size == "150X150") and x.depth > 7  and x.depth<=8]

    # s_150x150_0_2 = [x for x in s_list if (x.size == "150X150") and x.depth > 0  and x.depth<=2]
    # s_150x150_2_3 = [x for x in s_list if (x.size == "150X150") and x.depth > 2  and x.depth<=3]
    # s_150x150_3_4 = [x for x in s_list if (x.size == "150X150") and x.depth > 3  and x.depth<=4]
    # s_150x150_4_5 = [x for x in s_list if (x.size == "150X150") and x.depth > 4  and x.depth<=5]
    # s_150x150_5_6 = [x for x in s_list if (x.size == "150X150") and x.depth > 5  and x.depth<=6]
    # s_150x150_6_7 = [x for x in s_list if (x.size == "150X150") and x.depth > 6  and x.depth<=7]
    # s_150x150_7_8 = [x for x in s_list if (x.size == "150X150") and x.depth > 7  and x.depth<=8]

    # s_150x150_0_2 = [x for x in s_list if (x.size == "150X150") and x.depth > 0  and x.depth<=2]
    # s_150x150_2_3 = [x for x in s_list if (x.size == "150X150") and x.depth > 2  and x.depth<=3]
    # s_150x150_3_4 = [x for x in s_list if (x.size == "150X150") and x.depth > 3  and x.depth<=4]
    # s_150x150_4_5 = [x for x in s_list if (x.size == "150X150") and x.depth > 4  and x.depth<=5]
    # s_150x150_5_6 = [x for x in s_list if (x.size == "150X150") and x.depth > 5  and x.depth<=6]
    # s_150x150_6_7 = [x for x in s_list if (x.size == "150X150") and x.depth > 6  and x.depth<=7]
    # s_150x150_7_8 = [x for x in s_list if (x.size == "150X150") and x.depth > 7  and x.depth<=8]





    receptor_main = [x for x in s_list if x.is_receptor()]

