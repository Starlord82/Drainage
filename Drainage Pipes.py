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

pipe1 = Pipe('p-1',90,130,2.5)
print(pipe1.twidth())



        