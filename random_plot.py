import pandas
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import os
from test_report import test_report

# flags section

# assumes the following structure:
# root
# /data
# /images

class vibe_data_random(test_report):
    def __init__(self):
        self.filenames = []
        self.test_time = 0
        self.base_path = ""
        self.base_name = ""
        self.truth_x = [20,153,190,250,750,2000]
        self.truth_y = [.057,.057,.099,.099,.055,.18]
        super().__init__()
    def grab_filenames(self, base_name):
        self.base_name = base_name
        if (self.base_path != ""):
            base_path = self.base_path+"/data"
            for file in os.listdir(base_path):
                if ("." in file):
                    print("ignoring telem file")
                else:
                    self.filenames.append(base_path+"/"+file)
                print(os.path.join(base_path,file))
            self.filenames.sort()
            for f in self.filenames:
                print(f)
        else:
            return -1 
    def plot_data(self, file=-1, channel = -1, output_name = ""): # set file to anything above -1 to plot a specific element
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
            if (output_name == ""):
                plt.savefig(self.filenames[file]+".png")
            else:
                plt.savefig(output_name)
    def create_results(self):
        self.add_h2("Vibration Profile Stimulus: ")
        self.add_image("./images/Capture.PNG")
        self.add_h2("Before Vibration Pictures: ")
        self.add_images("before", sizew=1065, sizeh=763) # adds_images based upon partial match to filename
        self.add_h2("Vibration Data Results: ")
        self.grab_filenames(self.base_name)
        self.plot_data(file=0,channel=2, output_name = self.base_path+"/images/data.png")
        self.add_image("./images/data.png")
        self.add_h2("After Vibration Pictures: ")
        self.add_images("post",sizew=1065,sizeh=763)

if __name__ == "__main__":
    random_data = vibe_data_random()
    random_data.base_path = "/home/rommac/Downloads/Rand_CF1_X"
    random_data.title = "Battery CF1 X Axis Vibration Test"
    random_data.grab_filenames("Rand_CF1_X")
    random_data.test_date = "08-12-2022"
    random_data.analysis_date ="08-12-2022"
    random_data.output_dir = random_data.base_path
    random_data.test_type = "random vibe test"
    random_data.test_description_paragraph = "Battery Test CF1_X Results"
    random_data.test_description_short = "Battery Test CF1_X Results"
    random_data.write_html_report()

