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


def t47_2():
    # SVG creation for a simplified representation of the UN flag

    # SVG Header
    svg_header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <!-- Created with OpenAI (https://openai.com) -->
    """

    # SVG Content
    svg_content = f"""<svg
       width="315"
       height="273"
       viewBox="0 0 315 273"
       version="1.1"
       id="svg8"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:xlink="http://www.w3.org/1999/xlink"
       xml:space="preserve">
      <rect
         width="315"
         height="273"
         style="fill:#5b92e5"/>
      <circle
         cx="157.5"
         cy="136.5"
         r="65"
         style="fill:#fff"/>
      <path
         d="M 157.5,71.5 "
         style="fill:none;stroke:#fff;stroke-width:2"/>
      <!-- Simplified olive branches would go here -->
      <!-- World map simplified paths would go here -->
    </svg>
    """

    # Combine the header and content
    svg_code = svg_header + svg_content

    # Since this is a very simplified version, the paths for olive branches and world map are omitted.
    # Normally, you would include <path> elements with the "d" attribute defining the complex shapes.

    # Saving the SVG code to a file
    svg_filename = 'figure47_2.svg'
    with open(svg_filename, 'w') as svg_file:
        svg_file.write(svg_code)


if __name__ == "__main__":
    t47_2()
