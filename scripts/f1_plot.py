from sys import argv

import matplotlib.pyplot as plt

def calc_plot(fname):
    with open(fname, "r") as f:
        lines = f.readlines()

    f1_scores = []
    epoch_num = []

    for l in lines:
        if l.startswith("F1"):
            f1_scores.append(float(l.strip().split(":")[1]))
        elif l.startswith("Epoch"):
            epoch_num.append(int(l.strip().split(":")[1]))

    return f1_scores, epoch_num

if __name__ == "__main__":
    f1_beng, epoch_num = calc_plot(argv[1])
    plt.plot(epoch_num, f1_beng, label="Bengali")
    
    f1_hindi, epoch_num = calc_plot(argv[2])
    plt.plot(epoch_num, f1_hindi, label="Hindi")

    plt.xlabel("Epoch")
    plt.ylabel("F1 score")
    plt.legend()

    plt.show()
