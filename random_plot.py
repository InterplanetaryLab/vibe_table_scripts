import pandas
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import os

# flags section

class vibe_data_random:
    def __init__(self):
        self.filenames = []
        self.test_time = 0
        self.base_path = ""
        self.base_name = ""
    def grab_filenames(self, base_name):
        self.base_name = base_name
        if (self.base_path != ""):
            for file in os.listdir(self.base_path):
                if ("." in file):
                    print("ignoring telem file")
                else:
                    self.filenames.append(self.base_path+"/"+file)
                print(os.path.join(self.base_path,file))
            self.filenames.sort()
            for f in self.filenames:
                print(f)
        else:
            return -1 
    def plot_data(self, file=-1, channel = -1): # set file to anything above -1 to plot a specific element
        if (file== -1): # plt all files
            print("plotting all files")
        else:
            f = open(self.filenames[file],'r')
            line = f.readline()
            line_split = line.split(",")
            cont_g_rms = float(line_split[0])
            ch1_g_rms = float(line_split[1])
            ch2_g_rms = float(line_split[2])
            df = pandas.read_csv(self.filenames[file], skiprows=1)
            print(df)
            fig,ax = plt.subplots()
            if (channel == -1):
                xlabel = "Frequency (Hz) \n CH1: %f grms, CH2: %f grms" %(ch1_g_rms,ch2_g_rms)
                df.plot(x=4, y=[1,2], ax=ax,logy=True, title= ("ASD: %s: file: %d - Channel 1 & 2"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=[0.01,1], figsize=(8,8))
                #plt.text('test', 1))
            elif (channel == 1):
                xlabel = "Frequency (Hz) \n CH1: %f grms" %(ch1_g_rms)
                df.plot(x=4, y=1, logy=True, ax=ax,title= ("ASD: %s: file: %d - Channel 1"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=[0.01,1], figsize=(8,8))
            elif (channel == 2):
                xlabel = "Frequency (Hz) \n CH2: %f grms" %(ch2_g_rms)
                df.plot(x=4, y=2, logy=True, ax=ax,title= ("ASD: %s: file: %d - Channel 2"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=[0.01,1], figsize=(8,8))
            plt.show()


if __name__ == "__main__":
    random_data = vibe_data_random()
    random_data.base_path = "/home/rommac/vibe_table_plotting/random/Rand_CF1_X"
    random_data.grab_filenames("Rand_CF1_X")
    random_data.plot_data(file=0,channel=2)
