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
        self.truth_x = [20,153,190,250,750,2000]
        self.truth_y = [.057,.057,.099,.099,.055,.18]
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
            ylims= [.000002,50]
            yticks =[.000002,.000005,.00001,.00002,.00005,.0001,.0002,.0005,.001,.002,.005,.01,.02,.05,.1,.2,.5,1,2,5,10,20,50]
            if (channel == -1):
                xlabel = "Frequency (Hz) \n CH1: %f grms, CH2: %f grms" %(ch1_g_rms,ch2_g_rms)
                df.plot(x=4, y=[1,2], ax=ax,logy=True, title= ("PSD: %s: file: %d - Channel 1 & 2"%(self.base_name, file)), xlabel=xlabel, ylabel="PSD (g^2/Hz)", ylim=ylims, figsize=(8,8), yticks=yticks)
                #plt.text('test', 1))
            elif (channel == 1):
                xlabel = "Frequency (Hz) \n CH1: %f grms" %(ch1_g_rms)
                df.plot(x=4, y=1, logy=True, ax=ax,title= ("PSD: %s: file: %d - Channel 1"%(self.base_name, file)), xlabel=xlabel, ylabel="PSD (g^2/Hz)", ylim=ylims, figsize=(8,8), yticks=yticks)
            elif (channel == 2):
                xlabel = "Frequency (Hz) \n CH2: %f grms" %(ch2_g_rms)
                df.plot(x=4, y=2, logy=True, ax=ax,title= ("PSD: %s: file: %d - Channel 2"%(self.base_name, file)), xlabel=xlabel, ylabel="PSD (g^2/Hz)", ylim=ylims, figsize=(8,8), yticks=yticks)
            ax.plot(self.truth_x,self.truth_y)
            plt.show()


if __name__ == "__main__":
    random_data = vibe_data_random()
    random_data.base_path = "/home/rommac/Downloads/Rand_CF1_X"
    random_data.grab_filenames("Rand_CF1_X")
    random_data.plot_data(file=0,channel=2)
