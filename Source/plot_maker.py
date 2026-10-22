import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()

def get_data():
    plots = {}
    plt_cnt = 1
    
    while True:
        try:
            with open(f"Source/data/plot{plt_cnt}.csv", 'r') as f:
                r = f.read()
                try:
                    x, y = r.split('\n')
                    x = np.array([np.float64(i) for i in x.split(',')])
                    y = np.array([np.float64(i) for i in y.split(',')])
                    plots[f"plot{plt_cnt}"] = (x, y)
                except:
                    x = np.array([np.float64(i) for i in r.split(',')])
                    plots[f"plot{plt_cnt}"] = x
            plt_cnt += 1
        except:
            break

    return plots

plots = get_data()

def Plt_Config():

    fig, ax = plt.subplots()
    fig.set_dpi(250)
    fig.set_size_inches(3, 2)
    ax.tick_params(which = "minor", labelsize = 5, size = 2)
    ax.tick_params(which = "major", labelsize = 5, size = 4)

    return (fig, ax)

def plot1():
    fig, ax = Plt_Config()
    p1 = plots["plot1"]
    ax.hist(p1, bins = 15)
    ax.axvline(np.mean(p1), color = "Orange")
    
def plot2():
    fig, ax = Plt_Config()
    p2 = plots["plot2"]
    ax.hist(p2, bins = np.arange(24.5, 36, 1))
    ax.axvline(np.percentile(p2, 85), color = "Orange")
    
def plot3():
    fig, ax = Plt_Config()
    p3 = plots["plot3"]
    ax.hist(p3, bins = np.arange(0.25, 0.75, 1/100))
    ax.axvline(np.mean(p3), color = "Orange")
    ax.axvline(np.mean(p3) + np.std(p3), color = "Green")
    ax.axvline(np.mean(p3) - np.std(p3), color = "Green")
    
def plot4():
    fig, ax = Plt_Config()
    p4 = plots["plot4"]
    tails = np.mean(p4 == 0)
    heads = np.mean(p4 == 1)
    ax.bar(x = (0,1), height = (tails, heads), tick_label = ("Tails", "Heads"))
    ax.axhline(np.mean(plots["plot3"]), color = "Orange")
    ax.axhline(np.mean(plots["plot3"]) + np.std(plots["plot3"]), color = "Green")
    ax.axhline(np.mean(plots["plot3"]) - np.std(plots["plot3"]), color = "Green")
    
def plot5():
    fig, ax = Plt_Config()
    p5 = plots["plot5"]
    ax.hist(p5, bins = np.arange(0, 13))
    ax.axvline(np.mean(p5), color = "Orange")
    
def plot6():
    fig, ax = Plt_Config()
    p6 = plots["plot6"]
    ax.hist(p6, bins = 10)
    ax.axvline(np.percentile(p6, 90), color = "Orange")
    ax.axvline(np.percentile(p6, 10), color = "Orange")

def plot7():
    fig, ax = Plt_Config()
    p7 = plots["plot7"]
    ax.scatter(p7[0], p7[1], s = 0.5)
    lin = np.polyfit(p7[0], p7[1], 1)
    ax.axline((0, lin[1]), slope = lin[0], color = "Orange")