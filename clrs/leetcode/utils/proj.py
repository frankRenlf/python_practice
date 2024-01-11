# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/10 13:44 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""


# if __name__ == "__main__":
def t47_0():
    import matplotlib.pyplot as plt
    import numpy as np

    # Sample data points for the x-axis (number of images in millions)
    x = np.array([1, 10, 100, 1000])

    # Sample data points for the y-axis (CIDEr scores)
    y_base = np.array([50, 70, 85, 100])
    y_large = np.array([60, 80, 100, 120])
    y_huge = np.array([70, 90, 110, 140])

    # Plotting the curves
    plt.figure(figsize=(6, 4))
    plt.plot(x, y_base, 'b-*', label='Base')
    plt.plot(x, y_large, 'r-x', label='Large')
    plt.plot(x, y_huge, 'g-o', label='Huge')

    # Setting the x-axis to be logarithmic
    plt.xscale('log')

    # Adding titles and labels
    plt.title('Model performance as a function of pre-training dataset size')
    plt.xlabel('Million images in pre-training')
    plt.ylabel('CIDEr')

    # Adding a legend
    plt.legend()

    # Adding grid
    # plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig('figure47_0.png')
    # Display the plot
    plt.show()


def t47_1():
    import matplotlib.pyplot as plt
    import numpy as np
    # Task names and performance scores
    tasks = ['Caption', 'VQA', 'TR', 'IR', 'NLVR2']
    OSCaR_scores = [122, 72, 95, 90, 78]
    OSCaR_proportion = [100, 94, 100, 100, 100]
    MiniVLM_scores = [120, 70, 90, 85, 72]
    MiniVLM_proportion = [97, 96, 95, 95, 94]

    bar_width = 0.35  # width of the bars

    # Set position of bar on X axis
    r1 = np.arange(len(tasks))
    r2 = [x + bar_width for x in r1]

    # Make the plot
    plt.bar(r1, OSCaR_scores, color='blue', width=bar_width, label='OSCaR')
    plt.bar(r2, MiniVLM_scores, color='red', width=bar_width, label='MiniVLM (ours)')

    # Add text on top of the bars
    for i in range(len(tasks)):
        plt.text(r1[i], OSCaR_scores[i] + 3, f'{OSCaR_proportion[i]}%', ha='center', color='black')
        plt.text(r2[i], MiniVLM_scores[i] + 3, f'{MiniVLM_proportion[i]}%', ha='center', color='black')

    # Add xticks on the middle of the group bars
    plt.xlabel('Tasks', fontweight='bold')
    plt.xticks([r + bar_width / 2 for r in range(len(tasks))], tasks)

    # Create legend & Show graphic
    plt.legend()
    plt.savefig('figure47_1.png')

    plt.show()


if __name__ == "__main__":
    t47_0()
