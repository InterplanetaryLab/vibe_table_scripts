import pandas
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import os
from random_plot import vibe_data_random

class vibe_data_sine(vibe_data_random):
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
            ylims= [0, 10]
            if (channel == -1):
                xlabel = "Frequency (Hz) \n"
                df.plot(x=0, y=[1,2], ax=ax,logy=True, logx=True,title= ("ASD: %s: file: %d - Channel 1 & 2"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=ylims, figsize=(8,8))
                #plt.text('test', 1))
            elif (channel == 1):
                xlabel = "Frequency (Hz) \n"
                df.plot(x=0, y=2, logy=True, logx=True, ax=ax,title= ("ASD: %s: file: %d - Channel 1"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=ylims, figsize=(8,8))
            elif (channel == 2):
                xlabel = "Frequency (Hz) \n"
                df.plot(x=0, y=2, logy=True, logx=True, ax=ax,title= ("ASD: %s: file: %d - Channel 2"%(self.base_name, file)), xlabel=xlabel, ylabel="ASD (g^2/Hz)", ylim=ylims, figsize=(8,8))
            plt.show()


if __name__ == "__main__":
    sine_data = vibe_data_sine()
    sine_data.base_path = "/home/rommac/Downloads/SineTest 05-22-22 1523"
    sine_data.grab_filenames("SineTest 05-22-22 1523")
    sine_data.plot_data(file=0,channel=2)
