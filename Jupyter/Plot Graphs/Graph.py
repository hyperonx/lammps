import os
# from tkinter import *
from tkinter import filedialog,messagebox,Tk

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from itertools import cycle


sns.set()
plt.rcParams['figure.figsize'] = [11, 7]


class plotGraphs():
    def __init__(self):
        self.dir_name =""
        self.cycol = cycle('bgrcmk')
        self.ask_directory()
        self.file_name = r"npt_single_graphene.txt"
        self.file_path = os.path.join(self.dir_name, self.file_name)
        self.graphs_dir = os.path.join(self.dir_name, "Graphs")
        self.columns = ["Steps", "Temp", "AvgTemp", "SysPressure", "AvgPressure", "Volume",
                        "PE", "ETotal", "Density", "CO2Pressure"]
        self.make_graphs_directory()
        self.read_txt_file()
        self.plot_graphs()

    def ask_directory(self):
        root = Tk()
        root.withdraw()
        self.dir_name = filedialog.askdirectory()


    def make_graphs_directory(self):
        # print(self.graphs_dir)
        try:
            os.mkdir(self.graphs_dir)
        except:
            pass

    def read_txt_file(self):
        self.df = pd.read_csv(self.file_path, header=None, skiprows=2, delimiter="\s+", names=self.columns)

    def plot_graphs(self):
        x_ax = "Steps"
        y_cols = ["SysPressure (atm)", "CO2Pressure (atm)", "Volume", "Density (g/cc)", "Temp (K)"]
        for y in y_cols:
            y_ax = y.split(" ")[0]
            color = next(self.cycol)
            plt.plot(self.df[x_ax], self.df[y_ax], label=y, marker=".", color=color)
            plt.title(f'$\mu_p={self.df[y_ax].mean():.2f},\sigma={self.df[y_ax].std():.2f}$')
            plt.axhline(self.df[y_ax].mean(), color='g', linestyle='dashed', linewidth=2)
            plt.ylabel(y)
            plt.xlabel(x_ax)
            plt.legend()
            # plt.xticks(rotation=90)
            plt.savefig(os.path.join(self.graphs_dir, y_ax+".png"), dpi=300)
            plt.close()

            plt.hist(self.df[y_ax], 50, label=y_ax+ " Fluctuation",color=color)
            plt.title(f'$\mu_v={self.df[y_ax].mean():.2f},\sigma={self.df[y_ax].std():.2f}$')
            plt.xlabel(y)
            plt.legend()
            plt.savefig(os.path.join(self.graphs_dir, y_ax+"_hist.png"), dpi=500)
            plt.close()

        messagebox.showinfo(title="Done", message="All of your graphs plotted. Thank You!!")

plotGraphs()